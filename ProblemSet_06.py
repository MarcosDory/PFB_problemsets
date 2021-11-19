#Ex 1 escrevendo o script para a musica: 
print("Ex01:")
file_object=open("Python_06.txt","r")
contents=file_object.read()
print(contents)

contents=contents.upper()
print(contents)

object= open("Python_06.txt","r")
for line in object:
 line=line.rstrip()
 print(line)

#Ex:2 Inserindo valores na novo arquivo a partir do script:
print("Ex 2:")
Obj=open("Python_06_uc.txt","w")
Obj.write(contents)
print(Obj)

#Ex 3 Abra e imprima o complemento reverso de Python_06.seq.txt:
F=open("Python_06.seq.txt","r")
F2=F.read()
F2=F2.replace('A','t')
F2=F2.replace('T','a')
F2=F2.replace('C','g')
F2=F2.replace('G','c')
F2=F2.upper()
print("Complemento da sequencia de DNA: print F2 para observar ")

#Ex4 Conte o numero de linhas e palavras e indique o tamanho médio das linhas:
print("Ex 4")
Dna_Fasta=open("Python_06.fastq","r")
count=0
for line in Dna_Fasta:
 count+=1
print ("number of lines in Python_06.fastq:",count)

nWords=0
nLinhas=0
if line in Dna_Fasta:
 nLinhas = nLinhas+1
 nWords=len(line.split())
 print(nWords)
print(nLinhas)

#Ex5 Escrever um script que realize a analise de um arquivo FASTA e retorne os dados de forma organizada:
print("EX 5")
with open("Python_06.fastq","r") as file_object: 
 for line in file_object:
  line = line.rstrip()
  print(line) 

DNA5=open("Python_06.fastq","r")
DNA5=DNA5.read()
K=DNA5.split('/t')
print(K)
