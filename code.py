# Teleport Home
# Chef has traveled a long way, and now wants to get home.
# Chef is 
# D
# D kilometers away from home, and he can walk at a speed of 
# 1
# 1 kilometer per hour.
# Chef also has the ability to teleport. He can teleport for a distance of at most 
# T kilometers, which happens instantly and doesn't require any time.
# The teleport can be used at most once.
# Find the minimum time, in hours, that Chef needs to reach home.

d,t=map(int,input().split())
if d>t:
    print(d-t)
else:
    print(0)

# Passing Chain
# N
# N football players stand in a line in order to practice their passes.
# The players are numbered 
# 1
# 1 to 
# N
# N.
# Initially, player 
# 1
# 1 has the ball.
# All the players have a passing power of 
# K
# K.
# At any point of time, if player 
# X
# X has the ball:
# If 
# X
# +
# K
# ≤
# N
# X+K≤N, the ball will be passed to player 
# X
# +
# K
# X+K.
# Otherwise, the ball will remain with player 
# X
# X.
# You are given 
# N
# N and 
# K
# K. Find the number of the player who will have the ball in the end, given that player 
# 1
# 1 starts with it.

t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    p=1 
    while p+k<=n:
        p+=k 
    print(p)

# question number third 
# Carrot Collection
# Deep in a forest live a bear and a rabbit.

# The forest has 
# N
# N clearings, numbered from 
# 1
# 1 to 
# N
# N.
# Clearing 
# i
# i has 
# A
# i
# A 
# i
# ​
#   carrots growing in it.

# The bear patrols several zones of the forest - specifically, you are given integers 
# L
# L and 
# R
# R, such that the bear patrols clearings 
# L
# ,
# L
# +
# 1
# ,
# L
# +
# 2
# ,
# …
# ,
# R
# L,L+1,L+2,…,R.
# It is guaranteed that either 
# L
# >
# 1
# L>1 or 
# R
# <
# N
# R<N, i.e. there exists at least one clearing not patrolled by the bear.

# The rabbit wants to collect some of the carrots from the forest.
# This will be done via the following process:

# Let 
# X
# X be the current clearing the rabbit is in.
# The rabbit can do any one of the following three things:
# Take all carrots from clearing 
# X
# X. This is allowed only if clearing 
# X
# X still has carrots.
# Move to clearing 
# X
# −
# 1
# X−1. This is allowed only if 
# X
# >
# 1
# X>1.
# Move to clearing 
# X
# +
# 1
# X+1. This is allowed only if 
# X
# <
# N
# X<N.
# The left/right moves can be done as many times as you like, and it is allowed to visit the same clearing multiple times if you wish.
# However, the rabbit cannot visit any clearing that's being patrolled by the bear.

# The initial value of s
# X
# X can be chosen freely by the rabbit; as long as it is some clearing that's not patrolled.

# Find the maximum possible number of carrots the rabbit can collect under the above conditions.
# cook your dish here
t=int(input())
for i in range(t):
    n,l,r=map(int,input().split())
    arr=list(map(int,input().split()))
    s1=sum(arr[:l-1])
    s2=sum(arr[r:])
    print(max(s1,s2))

# new ques
# Movie Night
# Chef is watching a movie that lasts for 
# H
# H hours and 
# M
# M minutes.
# To plan the rest of his day efficiently, Chef wants to know the total duration of the movie completely in minutes.
# Help Chef find the total duration of the movie in minutes.
def getTotalDuration(H: int, M: int) -> int:
    p=(60*H)+M
    return p 

# ques 5 dsa code
# Find smallest and largest numbers
# Given an array of integers, your task is to find the smallest (minimum) and largest (maximum) elements present in the array.
# solution
def findMinMax(n: int, arr: list[int]) -> list[int]:
    p=max(arr)
    q=min(arr)
    return q,p

# dsa ques 6 anagram 
# You are given 
# N
# N strings consisting of lowercase English letters.
# Your goal is to find the longest string 
# W
# W such that the letters of 
# W
# W (including duplicates) appear in every string in the given set.
# Specifically, if a letter appears 
# k
# k times in 
# W
# W, it must appear at least 
# k
# k times in each of the 
# N
# N input strings.
# If there are multiple such strings of the maximum possible length, choose the one that is lexicographically smallest (i.e., in alphabetical order). If no such non-empty string can be formed, output no such string (without quotes).
n=int(input())
c=set(input())
for i in range(n-1):
    w=set(input())
    c&=w 
print("".join(sorted(c)))

# ques 7 codechef
# CodeChef XP
# Chef is active on CodeChef and earns XP by contributing to the platform.
# Solving a problem earns him A
# A XP.
# Writing an editorial earns him 
# B B XP.
# Today, Chef solved P problems and wrote E editorials. Find the total XP earned by Chef today.
import string
import sys
def main(a,b,c,d):
    p=a*c 
    q=b*d 
    return p+q 
a,b,c,d=map(int,input().split())
print(main(a,b,c,d))

# ques 8 codechef
# contest ques

# Chef loves his own name. So, he likes a word if and only if it either starts with the letter 'c', or ends with the letter 'f' (or both).
# You are given a string 
# S that represents a four-letter word.
# S contains only lowercase English letters
# Does Chef like the word represented by string 
s=input()
k=list(s)
if k[0]=="c" or k[-1]=="f":
    print("Yes")
else:
    print("No")

# 245 contest codechef
# ques- 
# Cooling Conundrum
# Chef is preparing a dessert, and as part of the process, needs to cool the dessert down a bit.
# The current temperature of the dessert is 
# X
# X degrees, and Chef wants it to be at 
# Y
# Y degrees (where 
# X
# >
# Y
# X>Y).
# Chef's refrigerator can cool the dessert, but the time it takes depends on the current temperature of the dish.
# Specifically, if the current temperature of the dish is 
# K degrees, then the refrigerator will take 
# 10
# 10 seconds, rounded up to the nearest integer, to reduce the temperature of the dish by 
# 1
# 1 degree.
import math
t=int(input())
for i in range(t):
    x=list(map(int,input().split()))
    m=0
    for i in range(x[0],x[1],-1):
        m+=math.ceil(i/10)
    print(m)
    
# ques3 codechef 
# Equivalent Exchange
# A certain shop sells two colors of stones: red stones and blue stones.
# Today, 
# N
# N customers, numbered 
# 1,2,…,N, will visit the shop in order.
# The 
# i
# i-th customer will request a trade with parameter 
#  , where:
# , then the 
# i
# i-th customer will give 
#   red stones to the shop, and wants 
#   blue stones in return.
#  <0, then the 
# i
# i-th customer will give 
#   blue stones to the shop, and wants 
#   red stones in return.
# It is guaranteed that 
# ​
#  =0 for all 
# 1≤i≤N.
# The shop can only hold a total of 
# K
# K stones.
# At the start of the day, before any customers enter, the shopkeeper will choose an integer 
# 0≤X≤K), and stock the shop with 
# X
# X red stones and 
# K−X blue stones.
# Determine if it is possible for the shopkeeper process all 
# N
# N trades without ever running out of stones of either color.
# More formally, determine if it is possible to choose 
# X
# X in such a way that the following condition holds:
# The number of red stones and the number of blue stones in the shop both remain non-negative at all points of time.
# solution 


    
