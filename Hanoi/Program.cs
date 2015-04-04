using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Hanoi
{
    class Program
    {
        static void Main(string[] args)
        {
            HanoiMove(4, 1, 2);
        }

        static void HanoiMove(int n, int a, int b)
        {
            if (n == 1)
            {
                Console.WriteLine(string.Format("{0}: {1} -> {2}", n, a, b));
            }
            else if (n > 1)
            {
                HanoiMove(n - 1, a, 6 - a - b);
                Console.WriteLine(string.Format("{0}: {1} -> {2}", n, a, b));
                HanoiMove(n - 1, 6 - a - b, b);
            }
        }
    }
}
