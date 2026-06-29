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
