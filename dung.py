def ara_ara():
    N={}
    while 1:
        src=input()
        temp=src.split()
        if len(temp)==1:
            start=src
            fin=input()
            break
        if N.get(temp[0]) is None:
            N[temp[0]]={temp[1]}
        else:
            N[temp[0]].add(temp[1])

        if N.get(temp[1]) is None:
            N[temp[1]]={temp[0]}
        else:
            N[temp[1]].add(temp[0])                   
    visited=set()
    q=[start] 
    while q:
        v=q.pop(0)
        if v == fin: return 'YES'
        if v not in visited:
            visited.add(v)
            q.extend(N[v]-visited)
    return 'NO'        
        


if __name__ == '__main__':
    print(ara_ara())
