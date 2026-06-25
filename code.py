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