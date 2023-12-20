#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pywebio')


# In[2]:


from pywebio.input import *
from pywebio.output import *


# In[3]:


def default():
    inp_graph=Graph(6)
    inp_graph.addedge(0, 1, 2) 
    inp_graph.addedge(0, 3, 1) 
    inp_graph.addedge(0, 4, 4) 
    inp_graph.addedge(1, 2, 3) 
    inp_graph.addedge(1, 3, 3) 
    inp_graph.addedge(1, 5, 7) 
    inp_graph.addedge(2, 3, 5) 
    inp_graph.addedge(2, 5, 8) 
    inp_graph.addedge(3, 4, 9)   
    put_table([
    ['u', 'v','w'],
    ['0','1','2' ],
    ['0','3','1'],
    ['0','4','4'],
    ['1','2','3'],
    ['1','3','3'],
    ['1','5','7'],
    ['2','3','5'],
    ['2','5','8'],
    ['3','4','9']])
    inp_graph.kruskal()


# In[4]:


def check_num(num):
    if num<0 :
        return "Only positive integers"
        popup("Error!","No negative allowed")
        toast('New message 🔔')


# In[5]:


def welcome():
    put_markdown("`SCL PACKAGE`")


# In[6]:


class Graph:
    
    #constructor
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[]
        
    #add edge to graph
    def addedge(self,u,v,w):
        self.graph.append([u,v,w])
       
       
    def findelmt(self,parent,i):
        if(parent[i]==i):
            return i
        return self.findelmt(parent,parent[i])
    
    #union by rank
    def merge(self,parent,rank,n1,n2):
        
        rootn1=self.findelmt(parent,n1)
        rootn2=self.findelmt(parent,n2)
        
        if(rank[rootn1]<rank[rootn2]):
            parent[rootn1]=rootn2
        elif(rank[rootn1]>rank[rootn2]):
            parent[rootn2]=rootn1
        else:
            parent[rootn2]=rootn1
            rank[n1]+=1
            
    def kruskal(self):
        
        self.graph=sorted(self.graph,key=lambda weight:weight[2])
        MST=[]
        #MST.append(self.graph[0])
        #MST.append(self.graph[1])
        
        n=0
        g=0
        parent=[]
        rank=[]
        
        for i in range(self.V):
            parent.append(i)
            rank.append(0)
            
        while n<self.V-1:
            u=self.graph[g][0]
            v=self.graph[g][1]
            w=self.graph[g][2]
            g+=1
            
            ranku=self.findelmt(parent,u);
            rankv=self.findelmt(parent,v)
            
            if(ranku!=rankv):
                MST.append([u,v,w])
                self.merge(parent,rank,u,v)
                n+=1
            else:
                continue;
        
        for i in range(0,len(MST)):
            print(MST[i])
            put_markdown(f"MST{MST[i]}")

        


# In[7]:


welcome()
check=radio("Do u want to enter the values or go with default?",options=['Enter','Default'])
print(check)


# In[8]:


if(check=='Default'):
    default()
else:
    info = input_group("DATA",[
  input('No. of vertices:', name='v',type=NUMBER,validate=check_num),
  input('No. of edges:', name='e', type=NUMBER,validate=check_num),
    ])     
    print("No. of vertices=",info['v'],"No. of edges=",info['e'])
    inp_graph=Graph(info['v']) 
    put_table([['u','v','w']])
    for i in range(0,info['e'],1):
        u_v_w = input_group("DATA",[
      input('u:', name='u',type=NUMBER,validate=check_num),
      input('v:', name='v', type=NUMBER,validate=check_num),
      input('w:',name='w',type=NUMBER,validate=check_num),
        ])
        put_table([[u_v_w['u'],u_v_w['v'],u_v_w['w']]])
        inp_graph.addedge(u_v_w['u'],u_v_w['v'],u_v_w['w'])
    put_markdown("MIN SPANNING OF THE GIVEN GRAPH:")
    inp_graph.kruskal()


# In[9]:


popup('MINIMAL SPANNING TREE ALGORITHM',"Kruskal's Algorithm Done")
toast('New message 🔔')

