using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
class Solution {

    static void Main(String[] args) {
        int n = Convert.ToInt32(Console.ReadLine());
        float positiveNumbers = 0, negativeNumbers=0, zeroes=0;
        string[] arr_temp = Console.ReadLine().Split(' ');
        int[] arr = Array.ConvertAll(arr_temp,Int32.Parse);
        foreach(var x in arr){
            if(x>0){
                positiveNumbers++;
            }else if(x<0){
                negativeNumbers++;
            } else{
                zeroes++;
            }
        }

        Console.WriteLine(((positiveNumbers/n)).ToString(".0#####"));
        Console.WriteLine(((negativeNumbers/n)).ToString(".0#####"));
        Console.WriteLine(((zeroes/n)).ToString(".0#####"));
    }   
}
