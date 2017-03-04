using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
class Solution {

    static void Main(String[] args) {
        int n = Convert.ToInt32(Console.ReadLine());
        int LeftToRight = 0, RightToLeft = 0;
        int[][] a = new int[n][];
        for(int a_i = 0; a_i < n; a_i++){
           string[] a_temp = Console.ReadLine().Split(' ');
           a[a_i] = Array.ConvertAll(a_temp,Int32.Parse);
        }
        for(int i=0;i<n;i++){
            for(int j=0; j<n; j++){
                if(i==j){
                    LeftToRight+=a[i][j];
                }
                if(j==n-i-1){
                    RightToLeft+=a[i][j];
                }
            }
        }
        Console.WriteLine(Math.Abs(LeftToRight-RightToLeft));
    }
}