n=int(input())
m=int(input())
data=[]
for x in range(n):
   v=int(input()) 
   data.append([v])
for x in range(n):
   d=int(input()) 
   data[x].append(d)
   data[x].append(0)
data.sort(key=lambda x: x[0]/x[1],reverse=True)
ans=[]
# while (m>0):
#     for x in range(len(data)-1):
#         if data[x][0]-data[x][1]*(data[x][2])>=data[x+1][0]-data[x+1][1]*(data[x+1][2]):
#             data[x][2]+=1
#             ans+=data[x][0]-data[x][1]*(data[x][2])
#             print(ans,m)
#         else:
#             data[x+1][2]+=1
#             ans+=data[x+1][0]-data[x+1][1]*(data[x+1][2])
#             print(ans,m )
#         m-=1
#         if m==0:
#             break
for x in range(len(data)):
    meals=m
    while(meals):
        ans.append(data[x][0]-data[x][1]*data[x][2])
        data[x][2]+=1
        meals-=1
ans.sort(reverse=True)
print(sum(ans[:m]))
            
        
        
    
