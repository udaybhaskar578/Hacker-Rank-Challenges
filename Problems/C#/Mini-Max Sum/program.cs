using System;
using System.Collections.Generic;
using System.IO;
class Solution {
    static void Main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution */
        string[] arr_temp = Console.ReadLine().Split(' ');
        long min = Int64.MaxValue, max = Int64.MinValue, sum = 0;
        long[] arr = Array.ConvertAll(arr_temp,Int64.Parse);
        for(int i=0;i<arr.Length;i++){
          for(int j=0;j<arr.Length;j++){
            if(i==j){
                continue;
            }
              sum+=arr[j];
        } 
            if(sum >= max){
                max = sum;
            }
            if(min > sum){
                min = sum;
            }
            sum=0;
        }
Console.WriteLine(min+" "+max);
    }
}