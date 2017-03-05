using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
class Solution {

    static void Main(String[] args) {
        
        int n = Convert.ToInt32(Console.ReadLine());
        StringBuilder builder = new StringBuilder();
        int j=0;
        for(int i=0;i<n;i++){
            j=n;
            while(j-- >i+1){
                builder.Append(" ");
            }
            while(j-->=0){
                 builder.Append("#");
            }
            Console.WriteLine(builder.ToString());
            builder.Clear();
        }
    }
}
