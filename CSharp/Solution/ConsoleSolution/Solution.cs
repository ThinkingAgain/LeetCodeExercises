using System;
using System.Collections.Generic;
using System.Text;

namespace ConsoleSolution
{
    class Solution
    {
        public int LengthOfLIS(int[] nums)
        {
            if (nums.Length == 0) return 0;
            List<List<List<int>>> lis = new List<List<List<int>>>();
            foreach (var x in nums)
            {
                if (lis.Count == 0)
                {
                    List<int> ori = new List<int>(new int[] { x });
                    List<List<int>> a = new List<List<int>>();
                    a.Add(ori);
                    lis.Add(a);
                    continue;
                }

                int flag = 0;
                for (int i = lis.Count - 1; i >= 0; i--)
                {
                    foreach (var ori in lis[i])
                    {
                        if (ori[ori.Count - 1] < x)
                        {
                            //copy
                            List<int> newOri = new List<int>(ori);
                            newOri.Add(x);

                            //append                            
                            if (i == lis.Count - 1)
                            {
                                List<List<int>> a = new List<List<int>>();
                                a.Add(newOri);
                                lis.Add(a);
                            }
                            else
                            {
                                lis[i + 1].Add(newOri);
                            }
                            flag = 1;
                            break;
                        }

                    }
                    if (flag == 1) break;

                }
                if (flag == 0)
                {
                    List<int> ori = new List<int>(new int[] { x });
                    lis[0].Add(ori);
                }


            }

            return lis[lis.Count - 1][0].Count;
        }

        /// <summary>
        /// 字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，
        /// 字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。
        /// 你可以假设字符串中只包含大小写英文字母（a至z）。        
        /// </summary>
        /// <param name="S"></param>
        /// <returns></returns>
        public string CompressString(string S)
        {
            StringBuilder t = new StringBuilder();
            int count = 0;
            char prev = S[0];
            foreach (var x in S)
            {
                if (x == prev) count++;
                else
                {
                    t.Append(prev);
                    t.Append(count);
                    prev = x;
                    count = 1;
                }
            }
            t.Append(prev.ToString() + count);
            return t.ToString();
        }

        /// <summary>
        /// 给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。
        /// 假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。
        /// 注意：每次拼写时，chars 中的每个字母都只能用一次。
        /// 返回词汇表 words 中你掌握的所有单词的 长度之和。
        /// <param name="words"></param>
        /// <param name="chars"></param>
        /// <returns></returns>
        public int CountCharacters(string[] words, string chars)
        {
            int count = 0;
            bool flag;
            Dictionary<char, int> charDic = new Dictionary<char, int>();
            foreach (var c in chars)
            {
                if (charDic.ContainsKey(c)) charDic[c]++;
                else charDic.Add(c, 1);
            }

            foreach (var x in words)
            {
                flag = true;
                HashSet<char> wordSet = new HashSet<char>(x);
                if (wordSet.IsSubsetOf(chars))
                {
                    Dictionary<char, int> d = new Dictionary<char, int>();
                    foreach (var c in x)
                    {
                        if (d.ContainsKey(c)) d[c]++;
                        else d.Add(c, 1);
                    }
                    foreach (var item in d)
                    {
                        if (item.Value > charDic[item.Key])
                        {
                            flag = false;
                            break;
                        }
                    }
                    if (flag) count += x.Length;
                }
            }

            return count;
        }

        /// <summary>
        /// 给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。
        /// 返回使 A 中的每个值都是唯一的最少操作次数。
        /// </summary>
        /// <param name="A"></param>
        /// <returns></returns>
        public int MinIncrementForUnique(int[] A)
        {
            if (A.Length < 2) return 0;
            int count = 0;
            Array.Sort(A);
            for (int i = 1; i < A.Length; i++)
            {
                if(A[i] <= A[i - 1])
                {
                    count += A[i - 1] + 1 - A[i];
                    A[i] = A[i-1] + 1;
                    
                }
            }
            return count;
        }
    }
}
