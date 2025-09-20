from Bio import SeqIO
record = SeqIO.read("brca1.fasta","fasta") 
sequence=str(record.seq)
codons=[sequence[i:i+3] for i in range (0,len(sequence),3)]
gc_count=sequence.count("G")+sequence.count("C")
at_count=sequence.count("A")+sequence.count("T")
atg_count=sequence.count("ATG")

total_length=len(sequence)
total_codons=len(codons)

gc_content=(gc_count/total_length)*100
at_content=(at_count/total_length)*100
atg_content=(atg_count/total_codons)*100
print("gc_content: {:.2f}% ".format(gc_content))
print("at_content: {:.2f}% ".format(at_content))
print("atg_content: {:.2f}% ".format(atg_content))

record = SeqIO.read("brca1.fasta", "fasta")
sequence = record.seq
reverse_complement = sequence.reverse_complement()
print(sequence[:100])
print(reverse_complement[:100])

trait_to_genes = {
    "bat_immunity": ["IFITM3", "TLR7", "STING", "IRF7"],
    "bat_echolocation": ["Prestin"],
    "bat_flight": ["ATP5A1", "NDUFV2"],
    "bat_wing_structure": ["FGF10", "TBX5"]
    }

trait = input("enter trait:")
genes=trait_to_genes.get(trait)

if genes:
    print(f"genes are:{trait}:{genes}") 
else:
    print("deta not found")
