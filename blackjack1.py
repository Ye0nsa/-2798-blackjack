n,m=map(int,input().split());
nl=list(map(int,input().split()));
sc=0; pre=0;

for a in nl:
  sc+=a;
  #print(f"1단계 {sc}")
  #print(f"현재 리스트 상황 : {nl}")
  for b in nl:
    if b==a: ##중복 되는 숫자 제거를 다시 만들어야함
        continue;
    else:
      sc+=b
    #print(f"2단계 {b} / {sc}")
    #print(f"현재 리스트 상황 : {nl}")
    
    for c in nl:
      if c==b or c==a: ##중복 되는 숫자 제거를 다시 만들어야함
        continue;
      else:
        sc+=c
      #print(f"3단계 {c} / {sc}")
      #print(f"현재 리스트 상황 : {nl}")
      if m>=sc and sc>pre:
        pre=sc;
        #print(f"현재 sc및 pre :{sc} / {pre} / {nl}")
        sc=sc-c
      else:
        sc=sc-c
        continue;
    sc=sc-b
  sc=sc-a

print(pre)