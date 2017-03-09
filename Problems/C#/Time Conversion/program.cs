//https://www.hackerrank.com/challenges/time-conversion

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
class Solution {

    static void Main(String[] args) {
        string time = Console.ReadLine();
        var hours = Int32.Parse(time.Split(':')[0]);
        hours = time.Substring(time.Length - 2) =="PM" ? (hours < 12 ? hours+12 : hours):(hours ==12 ?0:hours );
        Console.WriteLine(hours.ToString("D2")+time.Substring(2).Remove(time.Length - 2 -2));
    }
}
