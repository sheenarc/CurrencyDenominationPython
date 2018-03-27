'''
Created on Mar 26, 2018

@author: i821553
'''


dollar_value = 9378

number_of_coins = 0;

denominations = {}

leftover = 0;

denominations["100"] = dollar_value/100;
leftover = dollar_value%100;

denominations["20"] = leftover/20;
leftover = leftover%20;

denominations["5"] = leftover/5;
leftover = leftover%5;

denominations["1"] = leftover;


print "Total Number of Coins : "
print denominations["100"] + denominations["20"] + denominations["5"] + denominations["1"]

