using System;

namespace ConsoleSolution
{
    class Program
    {
        static void Main(string[] args)
        {
            Solution t = new Solution();
            //Console.WriteLine(t.LengthOfLIS(new int[] { 2,3,13,44,50,20,80,67,70,72,33,38,39 }));
            //Console.WriteLine(t.CompressString("aabcccccaaa"));
            //Console.WriteLine(t.CountCharacters(new string[] { "hello", "world", "leetcode" }, "welldonehoneyr"));
            Console.WriteLine(t.MinIncrementForUnique(new int[] { 3, 2, 1, 2, 1, 7 }));
        }
    }
}
