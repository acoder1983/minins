using System;
using System.Text;
using System.Net.Mail;
using System.Collections.Generic;

using System.Windows.Forms;

namespace PostHostWebIp
{
    static class Program
    {
        static string HostWebIp = null;
        /// <summary>
        /// 应用程序的主入口点。
        /// </summary>
        [STAThread]
        static void Main()
        {
            while (true)
            {
                try
                {
                    if(HostWebIp == Util.FetchHostWebIp())
                    {
                        System.Threading.Thread.Sleep(60000);
                        continue;
                    }
                    HostWebIp = Util.FetchHostWebIp();
                    MailMessage mail = new MailMessage();
                    // 指明邮件发送的地址，主题，内容等信息  
                    // 发信人的地址为登录收发器的地址，这个收发器相当于我们平时Web版的邮箱或者是OutLook中配置的邮箱  
                    string mailbox = "acoder1983@163.com";
                    mail.From = new MailAddress(mailbox);
                    mail.To.Add(mailbox);
                    mail.Subject = string.Format("{0} {1}", HostWebIp, DateTime.Now);
                    mail.SubjectEncoding = Encoding.Default;
                    //mailMessage.Body = richtbxBody.Text;
                    mail.BodyEncoding = Encoding.Default;
                    // 设置邮件正文不是Html格式的内容  
                    mail.IsBodyHtml = false;
                    // 设置邮件的优先级为普通优先级  
                    mail.Priority = MailPriority.Normal;

                
                    //SmtpClient是发送邮件的主体，这个构造函数是告知SmtpClient发送邮件时使用哪个SMTP服务器
                    System.Net.Mail.SmtpClient mailClient = new System.Net.Mail.SmtpClient("smtp.163.com");
                    //构建一个认证实例，这里是smtp服务器的地址
                    System.Net.NetworkCredential nc = new System.Net.NetworkCredential(mailbox, "Giszorro@1983");
                    //将认证实例赋予mailClient 这里是登陆smtp的用户名和密码
                    mailClient.Credentials = nc;
                    //千万不要再画蛇添足在“mailClient.Credentials = nc;”语句下再对mailclient.UseDefaultCredentials赋值了，不管是false还是true，都将导致程序运行出错    
                    mailClient.Send(mail);
                }
                catch (System.Exception)
                {

                }
            }
        }
    }
}
