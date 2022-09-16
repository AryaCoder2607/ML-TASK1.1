modern_family=['CLaiRe_DunPhY','PHiL_dUnpHY','GloRia_PrItcHETt','CaMeRoN_TuCKer','sTeLlA']
character=modern_family
#indices=list(enumerate(modern_family))
indices=[0,1,2,3,4]
for i in range(0,len(modern_family)):
    str=modern_family[i]
    str=str.lower()
    if('_' in str):
        str=str.replace('_','-')
    character[i]=str
    i=i+1
temp=list(map(lambda character:len(character),character))
indices = [sum(i) for i in zip(indices, temp)]
indices.sort()
indices.reverse()
Phew_finally = {indices[i]: character[i] for i in range(len(indices))}
print(Phew_finally)
