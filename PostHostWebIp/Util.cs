using System;
using System.IO;
using System.Net;
using System.Collections.Generic;

using System.Text;

namespace PostHostWebIp
{
    class Util
    {
        public static string FetchHostWebIp()
        {
            // Create a request for the URL. 		
            WebRequest request = WebRequest.Create("http://www.net.cn/static/customercare/yourip.asp");
            // If required by the server, set the credentials.
            request.Credentials = CredentialCache.DefaultCredentials;
            // Get the response.
            HttpWebResponse response = (HttpWebResponse)request.GetResponse();
            // Display the status.
            Console.WriteLine(response.StatusDescription);
            // Get the stream containing content returned by the server.
            Stream dataStream = response.GetResponseStream();
            // Open the stream using a StreamReader for easy access.
            StreamReader reader = new StreamReader(dataStream, Encoding.Default);
            // Read the content.
            string responseFromServer = reader.ReadToEnd();
            // Display the content.

            string ip = ExtractSubStr(responseFromServer, "您的本地上网IP是：<h2>", ",");

            dataStream.Close();
            response.Close();

            return ip;
        }

        public static string ExtractSubStr(string text, string keyBeg, string keyEnd)
        {
            string ret = string.Empty;
            int beg = text.IndexOf(keyBeg, 0);
            if (beg != -1)
            {
                int end = text.IndexOf(keyEnd, beg + keyBeg.Length);
                if (end != -1)
                {
                    beg += keyBeg.Length;
                    ret = text.Substring(beg, end - beg);
                }
            }
            return ret;
        }
    }
}
