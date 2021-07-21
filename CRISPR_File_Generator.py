import csv
import os


#Input: Directory for Spreeadsheet
#Input: Spreadsheet of genes, markers
#Input: Directory to save files to
#For Each guide of input Gene:
    #Output: CRISPR Vector File
    #Output: Deathstar Ins File
    #Output: Primers

# ****Define functions****
#Locates gene in chr csv file.
#input: gene of interest "Kpha####", chr.csv
#returns: array[gene_exon_start, gene_exon_end, is_complement]
def chr_search(gene, file):
    open(file, "rt")
    with open(file, "rt") as x:
        reader = csv.DictReader(x)
        column_1 = [row["1"]for row in reader]
        x.close()
    with open(file, "rt") as x:
        reader = csv.DictReader(x)
        column_2 = [row["2"]for row in reader]
        x.close()
    with open(file, "rt") as x:
        reader = csv.DictReader(x)
        column_3 = [row["3"]for row in reader]
        x.close()
    with open(file, "rt") as x:
        reader = csv.DictReader(x)
        column_4 = [row["4"]for row in reader]
        x.close()
    with open(file, "rt") as x:
        reader = csv.DictReader(x)
        column_5 = [row["5"]for row in reader]
        x.close()
    with open(file, "rt") as x:
        reader = csv.DictReader(x)
        column_6 = [row["6"]for row in reader]
        x.close()
    with open(file, "rt") as x:
        reader = csv.DictReader(x)
        column_7 = [row["7"]for row in reader]
        x.close()
    with open(file, "rt") as x:
        reader = csv.DictReader(x)
        column_8 = [row["8"]for row in reader]
        x.close()
    with open(file, "rt") as x:
        reader = csv.DictReader(x)
        column_9 = [row["9"]for row in reader]
        x.close()

    exon_coord_line = ""
    #now search for the gene and get it's coordinates
    for iteration, line in enumerate(column_2):
        if (line == "/label=Kpha" + i) and (line_last == "exon"):
            print(line_last)
            print("Found {} at line {}".format(gene, iteration))
            exon_coord_line = iteration - 1
            print(exon_coord_line)
            break

        line_last = line

    #searching column 3 for coordinate and storing
    for iteration, line in enumerate(column_3):
        if iteration == exon_coord_line:
            print("Exon coordinates are {} for {}".format(line, gene_i))
            exon_coords = line
            break

    #separate exon_coords string into first number and second number
    print(exon_coords)
    gene_exon_start = ""
    gene_exon_end = ""
    num_list =["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    gene_start_recorded = False
    complement = False
    for character in exon_coords:
        if character == "c":
            complement = True
        if gene_start_recorded == False:
            if character in num_list:
                gene_exon_start += character
            elif (character == "."):
                gene_start_recorded = True
        if gene_start_recorded == True:
            if character in num_list:
                gene_exon_end += character

    #return the coordinates
    print(gene_exon_start)
    print(gene_exon_end)
    gene_coord_array = [gene_exon_start, gene_exon_end, complement]
    return gene_coord_array


#gene_start and gene_end should be int vars
#complement is boolean
#returns: array[locus_seq_fwd, locus_seq_complement]
def locus_seq_string(file, gene_start, gene_end, complement, primer_label, primer_num_curr):
    #store all csv headers as iterable arrays
    open(file, "rt")
    with open(file, "rt") as x:
        reader = csv.DictReader(x)
        column_1 = [row["1"]for row in reader]
        x.close()
    with open(file, "rt") as x:
        reader = csv.DictReader(x)
        column_2 = [row["2"]for row in reader]
        x.close()
    with open(file, "rt") as x:
        reader = csv.DictReader(x)
        column_3 = [row["3"]for row in reader]
        x.close()
    with open(file, "rt") as x:
        reader = csv.DictReader(x)
        column_4 = [row["4"]for row in reader]
        x.close()
    with open(file, "rt") as x:
        reader = csv.DictReader(x)
        column_5 = [row["5"]for row in reader]
        x.close()
    with open(file, "rt") as x:
        reader = csv.DictReader(x)
        column_6 = [row["6"]for row in reader]
        x.close()
    with open(file, "rt") as x:
        reader = csv.DictReader(x)
        column_7 = [row["7"]for row in reader]
        x.close()
    with open(file, "rt") as x:
        reader = csv.DictReader(x)
        column_8 = [row["8"]for row in reader]
        x.close()
    with open(file, "rt") as x:
        reader = csv.DictReader(x)
        column_9 = [row["9"]for row in reader]
        x.close()


    #find "ORIGIN" in column 1, marking where seuqence starts
    print("Parsing {} for sequence origin".format(gene_i_chr))
    for iteration, line in enumerate(column_1):
        if line == "ORIGIN":
            seq_begin = iteration + 1
        elif line == "//":
            seq_end = iteration - 1
            print(seq_begin)
            print(seq_end)
    print("Found sequence origin coords. Concatenating chromosome as string.")


    chr_seq = ""
    for index, row in enumerate(column_2):
        if ((index >= seq_begin) and (index <= seq_end)):
            chr_seq += column_3[index] + column_4[index] + column_5[index] + column_6[index] + column_7[index] + column_8[index]

    print("Finished concatenating chromosome sequence")

    a = 0
    for character in chr_seq:
        a += 1

    print("Chromosome is {} bp long".format(a))

    print("Locating gene locus within chromosome.")
    gene_locus_seq = ""
    gene_locus_seq_complement = ""
    gene_locus_seq_fwd = ""
    n = 1
    b = 0
    if gene_i_complement == False:
        for character in chr_seq:
            if (n >= gene_start) and (n <= gene_end):
                gene_locus_seq_fwd += character
                if character == "a":
                    gene_locus_seq_complement += "t"
                elif character == "t":
                    gene_locus_seq_complement += "a"
                elif character == "c":
                    gene_locus_seq_complement += "g"
                elif character == "g":
                    gene_locus_seq_complement += "c"
                b += 1
            n += 1


    elif gene_i_complement == True:
        for character in chr_seq:
            if (n >= gene_start) and (n <= gene_end):
                gene_locus_seq_complement += character
                if character == "a":
                    gene_locus_seq_fwd += "t"
                elif character == "t":
                    gene_locus_seq_fwd += "a"
                elif character == "c":
                    gene_locus_seq_fwd += "g"
                elif character == "g":
                    gene_locus_seq_fwd += "c"
                b += 1
            n += 1
        gene_locus_seq_fwd = gene_locus_seq_fwd[::-1]
        gene_locus_seq_complement = gene_locus_seq_complement[::-1]

    print("Locus sequence is {} bp long".format(b))

    #Create primers
    primer_label_arr = []
    primer_seq_arr = []
    primer_desc_arr = []
    upstream_fwd = ""
    downstream_rev = ""
    for index, bp in enumerate(gene_locus_seq_fwd):
        if (index >= 0) and (index < 20):
            upstream_fwd += bp
        if (index >= 20):
            tm = primer_tm_calc(upstream_fwd)
            print("Calculated melting temp for {} is {}: ".format(primer_label + str(primer_num_curr), tm))
            if (tm > 56):
                break;
            else: upstream_fwd += bp
    primer_label_arr.append(primer_label + str(primer_num_curr))
    primer_seq_arr.append(upstream_fwd)
    primer_desc_arr.append("{}_Locus_fwd".format(gene_i))
    print("Primer {} stored with sequence {}".format(primer_label + str(primer_num_curr), upstream_fwd))

    primer_num_curr += 1

    for index, bp in enumerate(gene_locus_seq_complement[::-1]):
        if (index >= 0) and (index < 20):
            downstream_rev += bp
        if (index >= 20):
            tm = primer_tm_calc(downstream_rev)
            print("Calculated melting temp for {} is {}: ".format(primer_label + str(primer_num_curr), tm))
            if (tm > 56):
                break;
            else: downstream_rev += bp

    primer_label_arr.append(primer_label + str(primer_num_curr))
    primer_seq_arr.append(downstream_rev)
    primer_desc_arr.append("{}_Locus_rev".format(gene_i))
    print("Primer {} stored with sequence {}".format(primer_label + str(primer_num_curr), downstream_rev))

    locus = [gene_locus_seq_fwd, gene_locus_seq_complement, primer_num_curr, primer_label_arr, primer_seq_arr, primer_desc_arr]
    return locus

#Fetches guides for gene from SS
def gene_get_gRNA(file, gene):
    open(file, "rt")
    with open(file, "rt") as x:
        reader = csv.DictReader(x)
        column_ID = [row["#seqId"]for row in reader]
        x.close()
    with open(file, "rt") as x:
        reader = csv.DictReader(x)
        column_guides = [row["Guide Seq"]for row in reader]
        x.close()
        #initialize array
    guide_array = []
    guide_array_ind = 1

    for index, row in enumerate(column_ID):
        seq_id_current = row
        #if gene_id is in the row, store it in array
        if (seq_id_current.find(gene) != -1):
            print("Found instance {} of gene ID for {}; storing guide sequence.".format(guide_array_ind, gene))
            guide_array.append(column_guides[index])
            guide_array_ind += 1

    print(guide_array)
    return guide_array

def R_vec_create(guide, marker, directory):
    if marker == "kan":
        genbank_seq = """ORIGIN
1 tgtttcacgt tttgtagctt tataagcagc tttttcttga agcttaagta gagtagtgtg
61 aaaaagagac caagtacaaa atatccacct tctgggtttt agtatttgtg ctgagccgca
121 tgtgttgata agaggcgata aggtacagaa atgatttgct agcaatccat cattattgaa
181 gtgtgagtgg gcacctgata tcatggcttg tttattcaat agagtctgac atagtgaaag
241 ggagttatga aattgaagaa gactccatgg caggcatatg taaatatacc agccaatcct
301 actacattga tccgtgatag tttagtggta gaaccaccgc ttgtcgcgcg gtagaccggg
361 gttcaattcc ccgtcgcgga gc{}gttttaga gctagaaata
421 gcaagttaaa ataaggctag tccgttatca acttgaaaaa gtggcaccga gtcggtgctt
481 tttttttttt ttcgatgaga ggagtattcg tcaggccaca tggctttctt gttctggtcg
541 gatccatcgt tggatccccc acacaccata gcttcaaaat gtttctactc cttttttact
601 cttccagatt ttctcggact ccgcgcatcg ccgtaccact tcaaaacacc caagcacagc
661 atactaaatt ttccctcttt cttcctctag ggtgtcgtta attacccgta ctaaaggttt
721 ggaaaagaaa aaagagaccg cctcgtttct ttttcttcgt cgaaaaaggc aataaaaatt
781 tttatcacgt ttctttttct tgaaattttt ttttttagtt tttttctctt tcagtgacct
841 ccattgatat ttaagttaat aaacggtctt caatttctca agtttcagtt tcatttttct
901 tgttctatta caactttttt tacttcttgt tcattagaaa gaaagcatag caatctaatc
961 taaggggcgg tgttgacaat taatcatcgg catagtatat cggcatagta taatacgaca
1021 aggtgaggaa ctaaaccatg agccatattc aacgggaaac gtcttgctcg aggccgcgat
1081 taaattccaa catggatgct gatttatatg ggtataaatg ggctcgcgat aatgtcgggc
1141 aatcaggtgc gacaatctat cgattgtatg ggaagcccga tgcgccagag ttgtttctga
1201 aacatggcaa aggtagcgtt gccaatgatg ttacagatga gatggtcaga ctaaactggc
1261 tgacggaatt tatgcctctt ccgaccatca agcattttat ccgtactcct gatgatgcat
1321 ggttactcac cactgcgatc cccgggaaaa cagcattcca ggtattagaa gaatatcctg
1381 attcaggtga aaatattgtt gatgcgctgg cagtgttcct gcgccggttg cattcgattc
1441 ctgtttgtaa ttgtcctttt aacagcgatc gcgtatttcg tctcgctcag gcgcaatcac
1501 gaatgaataa cggtttggtt gatgcgagtg attttgatga cgagcgtaat ggctggcctg
1561 ttgaacaagt ctggaaagaa atgcataagc ttttgccatt ctcaccggat tcagtcgtca
1621 ctcatggtga tttctcactt gataacctta tttttgacga ggggaaatta ataggttgta
1681 ttgatgttgg acgagtcgga atcgcagacc gataccagga tcttgccatc ctatggaact
1741 gcctcggtga gttttctcct tcattacaga aacggctttt tcaaaaatat ggtattgata
1801 atcctgatat gaataaattg cagtttcatt tgatgctcga tgagtttttc taacacgtcc
1861 gacggcggcc cacgggtccc aggcctcgga gatccgtccc ccttttcctt tgtcgatatc
1921 atgtaattag ttatgtcacg cttacattca cgccctcccc ccacatccgc tctaaccgaa
1981 aaggaaggag ttagacaacc tgaagtctag gtccctattt atttttttat agttatgtta
2041 gtattaagaa cgttatttat atttcaaatt tttctttttt ttctgtacag acgcgtgtac
2101 gcatgtaaca ttatactgaa aaccttgctt gagaaggttt tgggacgctc gaaggcttta
2161 atttgcaagc tggagaccaa catgtgagca aaaggccagc aaaaggccag gaaccgtaaa
2221 aaggccgcgt tgctggcgtt tttccatagg ctccgccccc ctgacgagca tcacaaaaat
2281 cgacgctcaa gtcagaggtg gcgaaacccg acaggactat aaagatacca ggcgtttccc
2341 cctggaagct ccctcgtgcg ctctcctgtt ccgaccctgc cgcttaccgg atacctgtcc
2401 gcctttctcc cttcgggaag cgtggcgctt tctcaatgct cacgctgtag gtatctcagt
2461 tcggtgtagg tcgttcgctc caagctgggc tgtgtgcacg aaccccccgt tcagcccgac
2521 cgctgcgcct tatccggtaa ctatcgtctt gagtccaacc cggtaagaca cgacttatcg
2581 ccactggcag cagccactgg taacaggatt agcagagcga ggtatgtagg cggtgctaca
2641 gagttcttga agtggtggcc taactacggc tacactagaa ggacagtatt tggtatctgc
2701 gctctgctga agccagttac cttcggaaaa agagttggta gctcttgatc cggcaaacaa
2761 accaccgctg gtagcggtgg tttttttgtt tgcaagcagc agattacgcg cagaaaaaaa
2821 ggatctcaag aagatccttt gatcttttct acgggagagg gcaaataggc aggttcgcct
2881 tcgtcacgct aggaggcaat tctataagaa tgcactcgag ataagctggg ggaacattcg
2941 cgaaaatgaa acaagtcggc tgttatagta tatttattat aatattgaaa gatctcaaaa
3001 gactacttat ttttgaatga accaagtatg aaatcaacct atttggggtt gaccaaaata
3061 agtaaatatt aattgtcgag tctgacgctc agtggaacga aaactcacgt taagggattt
3121 tggtcatgag atcaagtcct tagacttggg agtcattaag taatagcaag gtaaagtaat
3181 acagggagtt caaggctcac ccgccagcca tattacagta aagtagaaaa gataaatcga
3241 tcaaagttac aaacaataac agtaaatgaa gaaaacatca atgttaacga acaaaataca
3301 aatatatcat gcttgtatta ttattatgtt aataaaataa attaaagctt caagcaattc
3361 acaccttcct cttcttcttg gggtcagccc tgctgtctcc accgagctga gagaggtcga
3421 ttcttgtttc atagagcccc gtaattgact gatgaatcag tgtggcgtcc aggacctcct
3481 ttgtagaggt gtaccgcttt ctgtctatgg tggtgtcgaa gtacttgaag gctgcaggcg
3541 cgcccaagtt ggtcagagta aacaagtgga taatgttttc tgcctgctcc ctgatgggct
3601 tatccctgtg cttattgtaa gcagaaagca ccttatcgag gttagcgtcg gcgaggatca
3661 ctcttttgga gaattcgctt atttgctcga tgatctcatc aaggtagtgt ttgtgttgtt
3721 ccacgaacag ctgcttctgc tcattatctt cgggagaccc tttgagcttt tcatagtggc
3781 tggccagata caagaaatta acgtatttag agggcagtgc cagctcgtta cctttctgca
3841 gctcgcccgc actagcgagc attcgtttcc ggccgttttc aagctcaaag agagagtact
3901 tgggaagctt aatgatgagg tcttttttga cctctttata tcctttcgcc tcgagaaagt
3961 cgatggggtt tttttcgaag cttgatcgct ccatgattgt gatgcccagc agttccttga
4021 cgcttttgag ttttttagac ttccctttct ccactttggc cacaaccagt acactgtaag
4081 cgactgtagg agaatcgaat ccgccgtatt tcttggggtc ccaatctttt ttgcgtgcga
4141 tcagcttgtc gctgttcctt ttcgggagga tactttcctt ggagaagcct ccggtctgta
4201 cttcggtctt tttaacgatg ttcacctgcg gcatggacag gaccttccgg actgtcgcga
4261 aatccctacc cttgtcccac acgatttctc ctgtttctcc gtttgtttcg ataagtggtc
4321 gcttccgaat ctctccattg gccagtgtaa tctcggtctt gaaaaaattc ataatattgc
4381 tgtaaaagaa gtacttagcg gtggccttgc ctatttcctg ctcagacttt gcgatcattt
4441 tcctaacatc gtacacttta tagtctccgt aaacaaattc agattcaagc ttgggatatt
4501 ttttgataag tgcagtgcct accactgcat tcaggtaggc atcatgcgca tggtggtaat
4561 tgttgatctc tctcacctta taaaactgaa agtcctttct gaaatctgag accagcttag
4621 acttcagagt aataactttc acctctcgaa tcagtttgtc attttcatcg tacttggtgt
4681 tcatgcgtga atcgagaatt tgggccacgt gcttggtgat ctggcgtgtc tcaacaagct
4741 gccttttgat gaagccggct ttatccaact cagacaggcc acctcgttca gccttagtca
4801 gattatcgaa cttccgttgt gtgatcagtt tggcgttcag cagctgccgc caataatttt
4861 tcattttctt gacaacttct tctgagggga cgttatcact cttccctcta tttttatcgg
4921 atcttgtcaa cactttatta tcaatagaat catctttgag aaaagactgg ggcacgatat
4981 gatccacgtc gtagtcggag agccgattga tgtccagttc ctgatccacg tacatgtccc
5041 tgccgttctg caggtagtac aggtagagct tctcattctg aagctgggtg ttttcaactg
5101 ggtgttcctt aaggatttgg gaccccagtt cttttatacc ctcttcaatc ctcttcatcc
5161 tttccctact gttcttctgt cccttctggg tagtttggtt ctctcgggcc atctcgataa
5221 cgatattctc gggcttatgc cttcccatta ctttgacgag ttcatccacg accttaacgg
5281 tctgcagtat tccctttttg atagctgggc tacctgcaag attagcgatg tgctcgtgaa
5341 gactgtcccc ctggccagaa acttgtgctt tctggatgtc ctccttaaag gtgagagagt
5401 catcatggat caactgcatg aagttccggt tggcaaatcc atcggactta agaaaatcca
5461 ggattgtctt tccactctgc ttgtctcgga tcccattgat cagttttctt gacagccgcc
5521 cccatcctgt atatcggcgc ctcttgagct gtttcatgac tttgtcgtcg aagagatgag
5581 cgtaagtttt caagcgttct tcaatcatct ccctatcttc aaacaacgta agggtgagga
5641 caatgtcctc aagaatgtcc tcgttctcct cattgtccag gaagtccttg tctttaatga
5701 ttttcaggag atcgtgatac gttcccaggg atgcgttgaa gcgatcctcc actccgctga
5761 tttcaacaga gtcgaaacat tcaatctttt tgaaatagtc ttctttgagc tgtttcacgg
5821 taactttccg gttcgtcttg aagaggaggt ccacgatagc tttcttctgc tctccagaca
5881 ggaatgctgg ctttctcatc ccttctgtga cgtatttgac cttggtgagc tcgttataaa
5941 ctgtgaagta ctcgtacagc agagagtgtt taggaagcac cttttcgtta ggcagatttt
6001 tatcaaagtt agtcatcctt tcgatgaagg actgggcaga ggccccctta tccacgactt
6061 cctcgaagtt ccagggagtg atggtctctt ctgatttgcg agtcatccac gcgaatctgg
6121 aatttccccg ggcgaggggg cctacatagt agggtatccg aaatgtgagg attttctcaa
6181 tcttttccct gttatctttc aaaaaggggt agaaatcctc ttgccgcctg aggatagcgt
6241 gcagttcgcc caggtgaatc tggtggggga tgcttccatt gtcgaaagtg cgctgtttgc
6301 gcaacagatc ttctctgtta agctttacca gcagctcctc ggtgccgtcc attttttcca
6361 agatgggctt aataaatttg taaaattcct cctggcttgc tccgccgtca atgtatccgg
6421 cgtagccatt tttagactga tcgaagaaaa tttccttgta cttctcaggc agttgctgtc
6481 tgacaagggc cttcagcaaa gtcaagtctt ggtggtgctc atcatagcgc ttgatcatac
6541 tagcgctcag cggagctttg gtgatctccg tgttcactcg cagaatatca ctcagcagaa
6601 tggcgtctga caggttcttt gccgccaaaa aaaggtctgc gtactggtcg ccgatctggg
6661 ccagcagatt gtcgagatca tcatcgtagg tgtctttgct cagttgaagc ttggcatctt
6721 cggccaggtc gaagttagat ttaaagttgg gggtcagccc gagtgacagg gcgataagat
6781 taccaaacag gccgttcttc ttctccccag ggagctgtgc gatgaggttt tcgagccgcc
6841 gggatttgga cagcctagcg ctcaggattg ctttggcgtc aactccggat gcgttgatcg
6901 ggttctcttc gaaaagctga ttgtaagtct gaaccagttg gataaagagt ttgtcgacat
6961 cgctgttgtc tgggttcagg tccccctcga tgaggaagtg tccccgaaat ttgatcatat
7021 gcgccagcgc gagatagatc aaccgcaagt cagccttatc agtactgtct acaagcttct
7081 tcctcagatg atatatggtt gggtactttt catggtacgc cacctcgtcc acgatattgc
7141 caaagattgg gtggcgctcg tgctttttat cctcctccac caaaaaggac tcctccagcc
7201 tatggaagaa agagtcatcc accttagcca tctcattact aaagatctcc tgcaggtagc
7261 agatccgatt ctttctgcgg gtatatctgc gccgtgctgt tcttttgagc cgcgtggctt
7321 cggccgtctc cccggagtcg aacaggaggg cgccaatgag gttcttcttt atgctgtggc
7381 gatcggtatt gcccagaact ttgaattttt tgctcggcac cttgtactcg tccgtaatga
7441 cggcccaacc gacgctgttt gtgccgatat cgagcccaat ggagtacttc ttgtccattt
7501 ttagatgtag attgttataa ttgtgtgttt caaccaagaa gacaaaagcc tgctagatgt
7561 gctgtattta tatcttttca ggaccagggt ggatcgtggt ttgcagcata tttcaagtgg
7621 ttctatattc gcgacggaag ccatcgaagc gtatagacgt cacatgagat ggctcatcga
7681 ttaggagcac aaacgccatt atcagacgtc tagattgaga ctgtacgaag ctcgttaatt
7741 gaacaagatt acatatgaat tacatgtttc aatctagcca atggctttgt caattcacca
7801 taacagtact gtgagggggg tgcgagagat cagtcttcat accttaacta tttcttgcgc
7861 agagacacta ccaggggacg gagcggagga acctgttcca tcggttaagg ttggtcctat
7921 gcatggggtc aagaagagga gggtagctat gcgccgactc aattgctgtc gtgatggctt
7981 gaagttaacc atccgtggtt agggccaatt gcaaggcaaa tttacggtga tcctctcttc
8041 tgttcaacgt ccctcactgt ttccaatgat acccggggac aacagaggtt attgaagata
8101 ccgcccggag gtaagtttaa acgggtgaga ggaaaattac cattgaacgg cccctaaaga
8161 atgttttacc ggggcgtaaa tttgttagct tctcttgctg gttgtgagtc ctgtccggtg
8221 cggacttgtg tcatgactag gaatctgggg ttgggactag aactgtttta gagttgatga
8281 ggtaaagtag gtgagataca tgcagtatgt atgattatgt aacgtataac atctctccta
8341 tgatgaattc actgttcctt agaaaaattg acagataact gccaagaaag atcacattta
8401 taacggttgc cttttgccat cgtttgttct ttaaatctca tttagcatgg tttggaattg
8461 tgtgattttg cccaggtact ttcctctcac tctttcatac catgggata""".format(guide)
    elif marker == "zeo":
         genbank_seq = """ORIGIN
1 tgtttcacgt tttgtagctt tataagcagc tttttcttga agcttaagta gagtagtgtg
61 aaaaagagac caagtacaaa atatccacct tctgggtttt agtatttgtg ctgagccgca
121 tgtgttgata agaggcgata aggtacagaa atgatttgct agcaatccat cattattgaa
181 gtgtgagtgg gcacctgata tcatggcttg tttattcaat agagtctgac atagtgaaag
241 ggagttatga aattgaagaa gactccatgg caggcatatg taaatatacc agccaatcct
301 actacattga tccgtgatag tttagtggta gaaccaccgc ttgtcgcgcg gtagaccggg
361 gttcaattcc ccgtcgcgga gc{}gttttaga gctagaaata
421 gcaagttaaa ataaggctag tccgttatca acttgaaaaa gtggcaccga gtcggtgctt
481 tttttttttt ttcgatgaga ggagtattcg tcaggccaca tggctttctt gttctggtcg
541 gatccatcgt tggatccccc acacaccata gcttcaaaat gtttctactc cttttttact
601 cttccagatt ttctcggact ccgcgcatcg ccgtaccact tcaaaacacc caagcacagc
661 atactaaatt ttccctcttt cttcctctag ggtgtcgtta attacccgta ctaaaggttt
721 ggaaaagaaa aaagagaccg cctcgtttct ttttcttcgt cgaaaaaggc aataaaaatt
781 tttatcacgt ttctttttct tgaaattttt ttttttagtt tttttctctt tcagtgacct
841 ccattgatat ttaagttaat aaacggtctt caatttctca agtttcagtt tcatttttct
901 tgttctatta caactttttt tacttcttgt tcattagaaa gaaagcatag caatctaatc
961 taaggggcgg tgttgacaat taatcatcgg catagtatat cggcatagta taatacgaca
1021 aggtgaggaa ctaaaccatg gccaagttga ccagtgccgt tccggtgctc accgcgcgcg
1081 acgtcgccgg agcggtcgag ttctggaccg accggctcgg gttctcccgg gacttcgtgg
1141 aggacgactt cgccggtgtg gtccgggacg acgtgaccct gttcatcagc gcggtccagg
1201 accaggtggt gccggacaac accctggcct gggtgtgggt gcgcggcctg gacgagctgt
1261 acgccgagtg gtcggaggtc gtgtccacga acttccggga cgcctccggg ccggccatga
1321 ccgagatcgg cgagcagccg tgggggcggg agttcgccct gcgcgacccg gccggcaact
1381 gcgtgcactt cgtggccgag gagcaggact gacacgtccg acggcggccc acgggtccca
1441 ggcctcggag atccgtcccc cttttccttt gtcgatatca tgtaattagt tatgtcacgc
1501 ttacattcac gccctccccc cacatccgct ctaaccgaaa aggaaggagt tagacaacct
1561 gaagtctagg tccctattta tttttttata gttatgttag tattaagaac gttatttata
1621 tttcaaattt ttcttttttt tctgtacaga cgcgtgtacg catgtaacat tatactgaaa
1681 accttgcttg agaaggtttt gggacgctcg aaggctttaa tttgcaagct ggagaccaac
1741 atgtgagcaa aaggccagca aaaggccagg aaccgtaaaa aggccgcgtt gctggcgttt
1801 ttccataggc tccgcccccc tgacgagcat cacaaaaatc gacgctcaag tcagaggtgg
1861 cgaaacccga caggactata aagataccag gcgtttcccc ctggaagctc cctcgtgcgc
1921 tctcctgttc cgaccctgcc gcttaccgga tacctgtccg cctttctccc ttcgggaagc
1981 gtggcgcttt ctcaatgctc acgctgtagg tatctcagtt cggtgtaggt cgttcgctcc
2041 aagctgggct gtgtgcacga accccccgtt cagcccgacc gctgcgcctt atccggtaac
2101 tatcgtcttg agtccaaccc ggtaagacac gacttatcgc cactggcagc agccactggt
2161 aacaggatta gcagagcgag gtatgtaggc ggtgctacag agttcttgaa gtggtggcct
2221 aactacggct acactagaag gacagtattt ggtatctgcg ctctgctgaa gccagttacc
2281 ttcggaaaaa gagttggtag ctcttgatcc ggcaaacaaa ccaccgctgg tagcggtggt
2341 ttttttgttt gcaagcagca gattacgcgc agaaaaaaag gatctcaaga agatcctttg
2401 atcttttcta cgggagaggg caaataggca ggttcgcctt cgtcacgcta ggaggcaatt
2461 ctataagaat gcactcgaga taagctgggg gaacattcgc gaaaatgaaa caagtcggct
2521 gttatagtat atttattata atattgaaag atctcaaaag actacttatt tttgaatgaa
2581 ccaagtatga aatcaaccta tttggggttg accaaaataa gtaaatatta attgtcgagt
2641 ctgacgctca gtggaacgaa aactcacgtt aagggatttt ggtcatgaga tcaagtcctt
2701 agacttggga gtcattaagt aatagcaagg taaagtaata cagggagttc aaggctcacc
2761 cgccagccat attacagtaa agtagaaaag ataaatcgat caaagttaca aacaataaca
2821 gtaaatgaag aaaacatcaa tgttaacgaa caaaatacaa atatatcatg cttgtattat
2881 tattatgtta ataaaataaa ttaaagcttc aagcaattca caccttcctc ttcttcttgg
2941 ggtcagccct gctgtctcca ccgagctgag agaggtcgat tcttgtttca tagagccccg
3001 taattgactg atgaatcagt gtggcgtcca ggacctcctt tgtagaggtg taccgctttc
3061 tgtctatggt ggtgtcgaag tacttgaagg ctgcaggcgc gcccaagttg gtcagagtaa
3121 acaagtggat aatgttttct gcctgctccc tgatgggctt atccctgtgc ttattgtaag
3181 cagaaagcac cttatcgagg ttagcgtcgg cgaggatcac tcttttggag aattcgctta
3241 tttgctcgat gatctcatca aggtagtgtt tgtgttgttc cacgaacagc tgcttctgct
3301 cattatcttc gggagaccct ttgagctttt catagtggct ggccagatac aagaaattaa
3361 cgtatttaga gggcagtgcc agctcgttac ctttctgcag ctcgcccgca ctagcgagca
3421 ttcgtttccg gccgttttca agctcaaaga gagagtactt gggaagctta atgatgaggt
3481 cttttttgac ctctttatat cctttcgcct cgagaaagtc gatggggttt ttttcgaagc
3541 ttgatcgctc catgattgtg atgcccagca gttccttgac gcttttgagt tttttagact
3601 tccctttctc cactttggcc acaaccagta cactgtaagc gactgtagga gaatcgaatc
3661 cgccgtattt cttggggtcc caatcttttt tgcgtgcgat cagcttgtcg ctgttccttt
3721 tcgggaggat actttccttg gagaagcctc cggtctgtac ttcggtcttt ttaacgatgt
3781 tcacctgcgg catggacagg accttccgga ctgtcgcgaa atccctaccc ttgtcccaca
3841 cgatttctcc tgtttctccg tttgtttcga taagtggtcg cttccgaatc tctccattgg
3901 ccagtgtaat ctcggtcttg aaaaaattca taatattgct gtaaaagaag tacttagcgg
3961 tggccttgcc tatttcctgc tcagactttg cgatcatttt cctaacatcg tacactttat
4021 agtctccgta aacaaattca gattcaagct tgggatattt tttgataagt gcagtgccta
4081 ccactgcatt caggtaggca tcatgcgcat ggtggtaatt gttgatctct ctcaccttat
4141 aaaactgaaa gtcctttctg aaatctgaga ccagcttaga cttcagagta ataactttca
4201 cctctcgaat cagtttgtca ttttcatcgt acttggtgtt catgcgtgaa tcgagaattt
4261 gggccacgtg cttggtgatc tggcgtgtct caacaagctg ccttttgatg aagccggctt
4321 tatccaactc agacaggcca cctcgttcag ccttagtcag attatcgaac ttccgttgtg
4381 tgatcagttt ggcgttcagc agctgccgcc aataattttt cattttcttg acaacttctt
4441 ctgaggggac gttatcactc ttccctctat ttttatcgga tcttgtcaac actttattat
4501 caatagaatc atctttgaga aaagactggg gcacgatatg atccacgtcg tagtcggaga
4561 gccgattgat gtccagttcc tgatccacgt acatgtccct gccgttctgc aggtagtaca
4621 ggtagagctt ctcattctga agctgggtgt tttcaactgg gtgttcctta aggatttggg
4681 accccagttc ttttataccc tcttcaatcc tcttcatcct ttccctactg ttcttctgtc
4741 ccttctgggt agtttggttc tctcgggcca tctcgataac gatattctcg ggcttatgcc
4801 ttcccattac tttgacgagt tcatccacga ccttaacggt ctgcagtatt ccctttttga
4861 tagctgggct acctgcaaga ttagcgatgt gctcgtgaag actgtccccc tggccagaaa
4921 cttgtgcttt ctggatgtcc tccttaaagg tgagagagtc atcatggatc aactgcatga
4981 agttccggtt ggcaaatcca tcggacttaa gaaaatccag gattgtcttt ccactctgct
5041 tgtctcggat cccattgatc agttttcttg acagccgccc ccatcctgta tatcggcgcc
5101 tcttgagctg tttcatgact ttgtcgtcga agagatgagc gtaagttttc aagcgttctt
5161 caatcatctc cctatcttca aacaacgtaa gggtgaggac aatgtcctca agaatgtcct
5221 cgttctcctc attgtccagg aagtccttgt ctttaatgat tttcaggaga tcgtgatacg
5281 ttcccaggga tgcgttgaag cgatcctcca ctccgctgat ttcaacagag tcgaaacatt
5341 caatcttttt gaaatagtct tctttgagct gtttcacggt aactttccgg ttcgtcttga
5401 agaggaggtc cacgatagct ttcttctgct ctccagacag gaatgctggc tttctcatcc
5461 cttctgtgac gtatttgacc ttggtgagct cgttataaac tgtgaagtac tcgtacagca
5521 gagagtgttt aggaagcacc ttttcgttag gcagattttt atcaaagtta gtcatccttt
5581 cgatgaagga ctgggcagag gcccccttat ccacgacttc ctcgaagttc cagggagtga
5641 tggtctcttc tgatttgcga gtcatccacg cgaatctgga atttccccgg gcgagggggc
5701 ctacatagta gggtatccga aatgtgagga ttttctcaat cttttccctg ttatctttca
5761 aaaaggggta gaaatcctct tgccgcctga ggatagcgtg cagttcgccc aggtgaatct
5821 ggtgggggat gcttccattg tcgaaagtgc gctgtttgcg caacagatct tctctgttaa
5881 gctttaccag cagctcctcg gtgccgtcca ttttttccaa gatgggctta ataaatttgt
5941 aaaattcctc ctggcttgct ccgccgtcaa tgtatccggc gtagccattt ttagactgat
6001 cgaagaaaat ttccttgtac ttctcaggca gttgctgtct gacaagggcc ttcagcaaag
6061 tcaagtcttg gtggtgctca tcatagcgct tgatcatact agcgctcagc ggagctttgg
6121 tgatctccgt gttcactcgc agaatatcac tcagcagaat ggcgtctgac aggttctttg
6181 ccgccaaaaa aaggtctgcg tactggtcgc cgatctgggc cagcagattg tcgagatcat
6241 catcgtaggt gtctttgctc agttgaagct tggcatcttc ggccaggtcg aagttagatt
6301 taaagttggg ggtcagcccg agtgacaggg cgataagatt accaaacagg ccgttcttct
6361 tctccccagg gagctgtgcg atgaggtttt cgagccgccg ggatttggac agcctagcgc
6421 tcaggattgc tttggcgtca actccggatg cgttgatcgg gttctcttcg aaaagctgat
6481 tgtaagtctg aaccagttgg ataaagagtt tgtcgacatc gctgttgtct gggttcaggt
6541 ccccctcgat gaggaagtgt ccccgaaatt tgatcatatg cgccagcgcg agatagatca
6601 accgcaagtc agccttatca gtactgtcta caagcttctt cctcagatga tatatggttg
6661 ggtacttttc atggtacgcc acctcgtcca cgatattgcc aaagattggg tggcgctcgt
6721 gctttttatc ctcctccacc aaaaaggact cctccagcct atggaagaaa gagtcatcca
6781 ccttagccat ctcattacta aagatctcct gcaggtagca gatccgattc tttctgcggg
6841 tatatctgcg ccgtgctgtt cttttgagcc gcgtggcttc ggccgtctcc ccggagtcga
6901 acaggagggc gccaatgagg ttcttcttta tgctgtggcg atcggtattg cccagaactt
6961 tgaatttttt gctcggcacc ttgtactcgt ccgtaatgac ggcccaaccg acgctgtttg
7021 tgccgatatc gagcccaatg gagtacttct tgtccatttt tagatgtaga ttgttataat
7081 tgtgtgtttc aaccaagaag acaaaagcct gctagatgtg ctgtatttat atcttttcag
7141 gaccagggtg gatcgtggtt tgcagcatat ttcaagtggt tctatattcg cgacggaagc
7201 catcgaagcg tatagacgtc acatgagatg gctcatcgat taggagcaca aacgccatta
7261 tcagacgtct agattgagac tgtacgaagc tcgttaattg aacaagatta catatgaatt
7321 acatgtttca atctagccaa tggctttgtc aattcaccat aacagtactg tgaggggggt
7381 gcgagagatc agtcttcata ccttaactat ttcttgcgca gagacactac caggggacgg
7441 agcggaggaa cctgttccat cggttaaggt tggtcctatg catggggtca agaagaggag
7501 ggtagctatg cgccgactca attgctgtcg tgatggcttg aagttaacca tccgtggtta
7561 gggccaattg caaggcaaat ttacggtgat cctctcttct gttcaacgtc cctcactgtt
7621 tccaatgata cccggggaca acagaggtta ttgaagatac cgcccggagg taagtttaaa
7681 cgggtgagag gaaaattacc attgaacggc ccctaaagaa tgttttaccg gggcgtaaat
7741 ttgttagctt ctcttgctgg ttgtgagtcc tgtccggtgc ggacttgtgt catgactagg
7801 aatctggggt tgggactaga actgttttag agttgatgag gtaaagtagg tgagatacat
7861 gcagtatgta tgattatgta acgtataaca tctctcctat gatgaattca ctgttcctta
7921 gaaaaattga cagataactg ccaagaaaga tcacatttat aacggttgcc ttttgccatc
7981 gtttgttctt taaatctcat ttagcatggt ttggaattgt gtgattttgc ccaggtactt
8041 tcctctcact ctttcatacc atgggata""".format(guide)
    elif marker == "nrs":
        genbank_seq = """ORIGIN
1 tgtttcacgt tttgtagctt tataagcagc tttttcttga agcttaagta gagtagtgtg
61 aaaaagagac caagtacaaa atatccacct tctgggtttt agtatttgtg ctgagccgca
121 tgtgttgata agaggcgata aggtacagaa atgatttgct agcaatccat cattattgaa
181 gtgtgagtgg gcacctgata tcatggcttg tttattcaat agagtctgac atagtgaaag
241 ggagttatga aattgaagaa gactccatgg caggcatatg taaatatacc agccaatcct
301 actacattga tccgtgatag tttagtggta gaaccaccgc ttgtcgcgcg gtagaccggg
361 gttcaattcc ccgtcgcgga gc{}gttttaga gctagaaata
421 gcaagttaaa ataaggctag tccgttatca acttgaaaaa gtggcaccga gtcggtgctt
481 tttttttttt ttcgatgaga ggagtattcg tcaggccaca tggctttctt gttctggtcg
541 gatccatcgt tggatccccc acacaccata gcttcaaaat gtttctactc cttttttact
601 cttccagatt ttctcggact ccgcgcatcg ccgtaccact tcaaaacacc caagcacagc
661 atactaaatt ttccctcttt cttcctctag ggtgtcgtta attacccgta ctaaaggttt
721 ggaaaagaaa aaagagaccg cctcgtttct ttttcttcgt cgaaaaaggc aataaaaatt
781 tttatcacgt ttctttttct tgaaattttt ttttttagtt tttttctctt tcagtgacct
841 ccattgatat ttaagttaat aaacggtctt caatttctca agtttcagtt tcatttttct
901 tgttctatta caactttttt tacttcttgt tcattagaaa gaaagcatag caatctaatc
961 taaggggcgg tgttgacaat taatcatcgg catagtatat cggcatagta taatacgaca
1021 aggtgaggaa ctaaaccatg ggtactactt tggacgacac cgcctacaga tacagaactt
1081 ctgttccagg tgacgctgag gctattgaag ctttggatgg ttccttcact accgacaccg
1141 ttttcagagt tactgctact ggtgacggtt tcaccttgag agaagttcca gttgacccac
1201 cactgaccaa ggttttccca gatgatgaat ctgacgacga atccgacgat ggtgaagatg
1261 gtgatccaga ctccagaact ttcgttgctt acggtgatga cggtgacttg gctggtttcg
1321 ttgttgtttc ttactccggt tggaaccgta gattgaccgt tgaggacatt gaagttgctc
1381 cagaacatag aggtcacggt gttggtagag ctttgatggg tcttgctact gagttcgcca
1441 gagaacgtgg tgctggtcat ttgtggttgg aggttacaaa cgttaacgct ccagctatcc
1501 acgcttacag aagaatgggt ttcaccctgt gtggtttgga cactgccttg tacgatggta
1561 ctgcttctga tggtgaacag gccttgtaca tgtctatgcc atgtccataa cacgtccgac
1621 ggcggcccac gggtcccagg cctcggagat ccgtccccct tttcctttgt cgatatcatg
1681 taattagtta tgtcacgctt acattcacgc cctcccccca catccgctct aaccgaaaag
1741 gaaggagtta gacaacctga agtctaggtc cctatttatt tttttatagt tatgttagta
1801 ttaagaacgt tatttatatt tcaaattttt cttttttttc tgtacagacg cgtgtacgca
1861 tgtaacatta tactgaaaac cttgcttgag aaggttttgg gacgctcgaa ggctttaatt
1921 tgcaagctgg agaccaacat gtgagcaaaa ggccagcaaa aggccaggaa ccgtaaaaag
1981 gccgcgttgc tggcgttttt ccataggctc cgcccccctg acgagcatca caaaaatcga
2041 cgctcaagtc agaggtggcg aaacccgaca ggactataaa gataccaggc gtttccccct
2101 ggaagctccc tcgtgcgctc tcctgttccg accctgccgc ttaccggata cctgtccgcc
2161 tttctccctt cgggaagcgt ggcgctttct caatgctcac gctgtaggta tctcagttcg
2221 gtgtaggtcg ttcgctccaa gctgggctgt gtgcacgaac cccccgttca gcccgaccgc
2281 tgcgccttat ccggtaacta tcgtcttgag tccaacccgg taagacacga cttatcgcca
2341 ctggcagcag ccactggtaa caggattagc agagcgaggt atgtaggcgg tgctacagag
2401 ttcttgaagt ggtggcctaa ctacggctac actagaagga cagtatttgg tatctgcgct
2461 ctgctgaagc cagttacctt cggaaaaaga gttggtagct cttgatccgg caaacaaacc
2521 accgctggta gcggtggttt ttttgtttgc aagcagcaga ttacgcgcag aaaaaaagga
2581 tctcaagaag atcctttgat cttttctacg ggagagggca aataggcagg ttcgccttcg
2641 tcacgctagg aggcaattct ataagaatgc actcgagata agctggggga acattcgcga
2701 aaatgaaaca agtcggctgt tatagtatat ttattataat attgaaagat ctcaaaagac
2761 tacttatttt tgaatgaacc aagtatgaaa tcaacctatt tggggttgac caaaataagt
2821 aaatattaat tgtcgagtct gacgctcagt ggaacgaaaa ctcacgttaa gggattttgg
2881 tcatgagatc aagtccttag acttgggagt cattaagtaa tagcaaggta aagtaataca
2941 gggagttcaa ggctcacccg ccagccatat tacagtaaag tagaaaagat aaatcgatca
3001 aagttacaaa caataacagt aaatgaagaa aacatcaatg ttaacgaaca aaatacaaat
3061 atatcatgct tgtattatta ttatgttaat aaaataaatt aaagcttcaa gcaattcaca
3121 ccttcctctt cttcttgggg tcagccctgc tgtctccacc gagctgagag aggtcgattc
3181 ttgtttcata gagccccgta attgactgat gaatcagtgt ggcgtccagg acctcctttg
3241 tagaggtgta ccgctttctg tctatggtgg tgtcgaagta cttgaaggct gcaggcgcgc
3301 ccaagttggt cagagtaaac aagtggataa tgttttctgc ctgctccctg atgggcttat
3361 ccctgtgctt attgtaagca gaaagcacct tatcgaggtt agcgtcggcg aggatcactc
3421 ttttggagaa ttcgcttatt tgctcgatga tctcatcaag gtagtgtttg tgttgttcca
3481 cgaacagctg cttctgctca ttatcttcgg gagacccttt gagcttttca tagtggctgg
3541 ccagatacaa gaaattaacg tatttagagg gcagtgccag ctcgttacct ttctgcagct
3601 cgcccgcact agcgagcatt cgtttccggc cgttttcaag ctcaaagaga gagtacttgg
3661 gaagcttaat gatgaggtct tttttgacct ctttatatcc tttcgcctcg agaaagtcga
3721 tggggttttt ttcgaagctt gatcgctcca tgattgtgat gcccagcagt tccttgacgc
3781 ttttgagttt tttagacttc cctttctcca ctttggccac aaccagtaca ctgtaagcga
3841 ctgtaggaga atcgaatccg ccgtatttct tggggtccca atcttttttg cgtgcgatca
3901 gcttgtcgct gttccttttc gggaggatac tttccttgga gaagcctccg gtctgtactt
3961 cggtcttttt aacgatgttc acctgcggca tggacaggac cttccggact gtcgcgaaat
4021 ccctaccctt gtcccacacg atttctcctg tttctccgtt tgtttcgata agtggtcgct
4081 tccgaatctc tccattggcc agtgtaatct cggtcttgaa aaaattcata atattgctgt
4141 aaaagaagta cttagcggtg gccttgccta tttcctgctc agactttgcg atcattttcc
4201 taacatcgta cactttatag tctccgtaaa caaattcaga ttcaagcttg ggatattttt
4261 tgataagtgc agtgcctacc actgcattca ggtaggcatc atgcgcatgg tggtaattgt
4321 tgatctctct caccttataa aactgaaagt cctttctgaa atctgagacc agcttagact
4381 tcagagtaat aactttcacc tctcgaatca gtttgtcatt ttcatcgtac ttggtgttca
4441 tgcgtgaatc gagaatttgg gccacgtgct tggtgatctg gcgtgtctca acaagctgcc
4501 ttttgatgaa gccggcttta tccaactcag acaggccacc tcgttcagcc ttagtcagat
4561 tatcgaactt ccgttgtgtg atcagtttgg cgttcagcag ctgccgccaa taatttttca
4621 ttttcttgac aacttcttct gaggggacgt tatcactctt ccctctattt ttatcggatc
4681 ttgtcaacac tttattatca atagaatcat ctttgagaaa agactggggc acgatatgat
4741 ccacgtcgta gtcggagagc cgattgatgt ccagttcctg atccacgtac atgtccctgc
4801 cgttctgcag gtagtacagg tagagcttct cattctgaag ctgggtgttt tcaactgggt
4861 gttccttaag gatttgggac cccagttctt ttataccctc ttcaatcctc ttcatccttt
4921 ccctactgtt cttctgtccc ttctgggtag tttggttctc tcgggccatc tcgataacga
4981 tattctcggg cttatgcctt cccattactt tgacgagttc atccacgacc ttaacggtct
5041 gcagtattcc ctttttgata gctgggctac ctgcaagatt agcgatgtgc tcgtgaagac
5101 tgtccccctg gccagaaact tgtgctttct ggatgtcctc cttaaaggtg agagagtcat
5161 catggatcaa ctgcatgaag ttccggttgg caaatccatc ggacttaaga aaatccagga
5221 ttgtctttcc actctgcttg tctcggatcc cattgatcag ttttcttgac agccgccccc
5281 atcctgtata tcggcgcctc ttgagctgtt tcatgacttt gtcgtcgaag agatgagcgt
5341 aagttttcaa gcgttcttca atcatctccc tatcttcaaa caacgtaagg gtgaggacaa
5401 tgtcctcaag aatgtcctcg ttctcctcat tgtccaggaa gtccttgtct ttaatgattt
5461 tcaggagatc gtgatacgtt cccagggatg cgttgaagcg atcctccact ccgctgattt
5521 caacagagtc gaaacattca atctttttga aatagtcttc tttgagctgt ttcacggtaa
5581 ctttccggtt cgtcttgaag aggaggtcca cgatagcttt cttctgctct ccagacagga
5641 atgctggctt tctcatccct tctgtgacgt atttgacctt ggtgagctcg ttataaactg
5701 tgaagtactc gtacagcaga gagtgtttag gaagcacctt ttcgttaggc agatttttat
5761 caaagttagt catcctttcg atgaaggact gggcagaggc ccccttatcc acgacttcct
5821 cgaagttcca gggagtgatg gtctcttctg atttgcgagt catccacgcg aatctggaat
5881 ttccccgggc gagggggcct acatagtagg gtatccgaaa tgtgaggatt ttctcaatct
5941 tttccctgtt atctttcaaa aaggggtaga aatcctcttg ccgcctgagg atagcgtgca
6001 gttcgcccag gtgaatctgg tgggggatgc ttccattgtc gaaagtgcgc tgtttgcgca
6061 acagatcttc tctgttaagc tttaccagca gctcctcggt gccgtccatt ttttccaaga
6121 tgggcttaat aaatttgtaa aattcctcct ggcttgctcc gccgtcaatg tatccggcgt
6181 agccattttt agactgatcg aagaaaattt ccttgtactt ctcaggcagt tgctgtctga
6241 caagggcctt cagcaaagtc aagtcttggt ggtgctcatc atagcgcttg atcatactag
6301 cgctcagcgg agctttggtg atctccgtgt tcactcgcag aatatcactc agcagaatgg
6361 cgtctgacag gttctttgcc gccaaaaaaa ggtctgcgta ctggtcgccg atctgggcca
6421 gcagattgtc gagatcatca tcgtaggtgt ctttgctcag ttgaagcttg gcatcttcgg
6481 ccaggtcgaa gttagattta aagttggggg tcagcccgag tgacagggcg ataagattac
6541 caaacaggcc gttcttcttc tccccaggga gctgtgcgat gaggttttcg agccgccggg
6601 atttggacag cctagcgctc aggattgctt tggcgtcaac tccggatgcg ttgatcgggt
6661 tctcttcgaa aagctgattg taagtctgaa ccagttggat aaagagtttg tcgacatcgc
6721 tgttgtctgg gttcaggtcc ccctcgatga ggaagtgtcc ccgaaatttg atcatatgcg
6781 ccagcgcgag atagatcaac cgcaagtcag ccttatcagt actgtctaca agcttcttcc
6841 tcagatgata tatggttggg tacttttcat ggtacgccac ctcgtccacg atattgccaa
6901 agattgggtg gcgctcgtgc tttttatcct cctccaccaa aaaggactcc tccagcctat
6961 ggaagaaaga gtcatccacc ttagccatct cattactaaa gatctcctgc aggtagcaga
7021 tccgattctt tctgcgggta tatctgcgcc gtgctgttct tttgagccgc gtggcttcgg
7081 ccgtctcccc ggagtcgaac aggagggcgc caatgaggtt cttctttatg ctgtggcgat
7141 cggtattgcc cagaactttg aattttttgc tcggcacctt gtactcgtcc gtaatgacgg
7201 cccaaccgac gctgtttgtg ccgatatcga gcccaatgga gtacttcttg tccattttta
7261 gatgtagatt gttataattg tgtgtttcaa ccaagaagac aaaagcctgc tagatgtgct
7321 gtatttatat cttttcagga ccagggtgga tcgtggtttg cagcatattt caagtggttc
7381 tatattcgcg acggaagcca tcgaagcgta tagacgtcac atgagatggc tcatcgatta
7441 ggagcacaaa cgccattatc agacgtctag attgagactg tacgaagctc gttaattgaa
7501 caagattaca tatgaattac atgtttcaat ctagccaatg gctttgtcaa ttcaccataa
7561 cagtactgtg aggggggtgc gagagatcag tcttcatacc ttaactattt cttgcgcaga
7621 gacactacca ggggacggag cggaggaacc tgttccatcg gttaaggttg gtcctatgca
7681 tggggtcaag aagaggaggg tagctatgcg ccgactcaat tgctgtcgtg atggcttgaa
7741 gttaaccatc cgtggttagg gccaattgca aggcaaattt acggtgatcc tctcttctgt
7801 tcaacgtccc tcactgtttc caatgatacc cggggacaac agaggttatt gaagataccg
7861 cccggaggta agtttaaacg ggtgagagga aaattaccat tgaacggccc ctaaagaatg
7921 ttttaccggg gcgtaaattt gttagcttct cttgctggtt gtgagtcctg tccggtgcgg
7981 acttgtgtca tgactaggaa tctggggttg ggactagaac tgttttagag ttgatgaggt
8041 aaagtaggtg agatacatgc agtatgtatg attatgtaac gtataacatc tctcctatga
8101 tgaattcact gttccttaga aaaattgaca gataactgcc aagaaagatc acatttataaGCAAT
8161 cggttgcctt ttgccatcgt ttgttcttta aatctcattt agcatggttt ggaattgtgt
8221 gattttgccc aggtactttc ctctcactct ttcataccat gggata""".format(guide)

    genbank_full =  """LOCUS       Exported                8509 bp DNA     circular SYN 03-JUN-2021
DEFINITION  synthetic circular DNA
ACCESSION   .
VERSION     .
KEYWORDS    .
SOURCE      synthetic DNA construct
  ORGANISM  synthetic DNA construct
REFERENCE   1  (bases 1 to 8509)
  AUTHORS
  TITLE     Direct Submission
  JOURNAL

FEATURES             Location/Qualifiers
     source          1..8509
                     /organism=“synthetic DNA construct”
                     /mol_type=“other DNA”
     promoter        10..382
                     /label=PG2
     promoter        10..310
                     /label=PG1
     tRNA            311..382
                     /label=PptRNA
     misc_feature    383..402
                     /label={}
     ncRNA           403..482
                     /label=stgRNA
                     /ncRNA_class=“guide_RNA”
     misc_RNA        403..478
                     /label=gRNA scaffold
                     /note=“guide RNA scaffold for the Streptococcus pyogenes
                     CRISPR/Cas9 system”
     terminator      483..492
                     /label=PTS
     misc_feature    493..552
                     /label=R5
     promoter        553..964
                     /gene=“S. cerevisiae TEF1”
                     /label=TEF1 promoter
                     /note=“promoter for EF-1-alpha”
     promoter        970..1037
                     /label=EM7 promoter
     promoter        972..1019
                     /label=EM7 promoter
                     /note=“synthetic bacterial promoter “
     CDS             1038..1853
                     /codon_start=1
                     /gene=“aph(3')-Ia”
                     /product=“aminoglycoside phosphotransferase”
                     /label={}R
                     /note=“confers resistance to kanamycin in bacteria or G418
                     (Geneticin(R)) in eukaryotes”
                     /translation=“MSHIQRETSCSRPRLNSNMDADLYGYKWARDNVGQSGATIYRLYG
                     KPDAPELFLKHGKGSVANDVTDEMVRLNWLTEFMPLPTIKHFIRTPDDAWLLTTAIPGK
                     TAFQVLEEYPDSGENIVDALAVFLRRLHSIPVCNCPFNSDRVFRLAQAQSRMNNGLVDA
                     SDFDDERNGWPVEQVWKEMHKLLPFSPDSVVTHGDFSLDNLIFDEGKLIGCIDVGRVGI
                     ADRYQDLAILWNCLGEFSPSLQKRLFQKYGIDNPDMNKLQFHLMLDEFF”
     terminator      1919..2166
                     /gene=“S. cerevisiae CYC1”
                     /label=CYC1 terminator
                     /note=“transcription terminator for CYC1”
     rep_origin      complement(2182..2855)
                     /direction=LEFT
                     /label=pUC origin
     rep_origin      complement(2241..2829)
                     /direction=LEFT
                     /label=ori
                     /note=“high-copy-number ColE1/pMB1/pBR322/pUC origin of
                     replication”
     misc_feature    2856..2915
                     /label=R2
     rep_origin      2916..3079
                     /label=PARS1
     misc_feature    3135..3154
                     /label=R4
     terminator      complement(3155..3358)
                     /label=pPtefTT
     CDS             complement(3361..7497)
                     /codon_start=3
                     /label=Cas9
                     /translation=“DKKYSIGLDIGTNSVGWAVITDEYKVPSKKFKVLGNTDRHSIKKN
                     LIGALLFDSGETAEATRLKRTARRRYTRRKNRICYLQEIFSNEMAKVDDSFFHRLEESF
                     LVEEDKKHERHPIFGNIVDEVAYHEKYPTIYHLRKKLVDSTDKADLRLIYLALAHMIKF
                     RGHFLIEGDLNPDNSDVDKLFIQLVQTYNQLFEENPINASGVDAKAILSARLSKSRRLE
                     NLIAQLPGEKKNGLFGNLIALSLGLTPNFKSNFDLAEDAKLQLSKDTYDDDLDNLLAQI
                     GDQYADLFLAAKNLSDAILLSDILRVNTEITKAPLSASMIKRYDEHHQDLTLLKALVRQ
                     QLPEKYKEIFFDQSKNGYAGYIDGGASQEEFYKFIKPILEKMDGTEELLVKLNREDLLR
                     KQRTFDNGSIPHQIHLGELHAILRRQEDFYPFLKDNREKIEKILTFRIPYYVGPLARGN
                     SRFAWMTRKSEETITPWNFEEVVDKGASAQSFIERMTNFDKNLPNEKVLPKHSLLYEYF
                     TVYNELTKVKYVTEGMRKPAFLSGEQKKAIVDLLFKTNRKVTVKQLKEDYFKKIECFDS
                     VEISGVEDRFNASLGTYHDLLKIIKDKDFLDNEENEDILEDIVLTLTLFEDREMIEERL
                     KTYAHLFDDKVMKQLKRRRYTGWGRLSRKLINGIRDKQSGKTILDFLKSDGFANRNFMQ
                     LIHDDSLTFKEDIQKAQVSGQGDSLHEHIANLAGSPAIKKGILQTVKVVDELVKVMGRH
                     KPENIVIEMARENQTTQKGQKNSRERMKRIEEGIKELGSQILKEHPVENTQLQNEKLYL
                     YYLQNGRDMYVDQELDINRLSDYDVDHIVPQSFLKDDSIDNKVLTRSDKNRGKSDNVPS
                     EEVVKKMKNYWRQLLNAKLITQRKFDNLTKAERGGLSELDKAGFIKRQLVETRQITKHV
                     AQILDSRMNTKYDENDKLIREVKVITLKSKLVSDFRKDFQFYKVREINNYHHAHDAYLN
                     AVVGTALIKKYPKLESEFVYGDYKVYDVRKMIAKSEQEIGKATAKYFFYSNIMNFFKTE
                     ITLANGEIRKRPLIETNGETGEIVWDKGRDFATVRKVLSMPQVNIVKKTEVQTGGFSKE
                     SILPKRNSDKLIARKKDWDPKKYGGFDSPTVAYSVLVVAKVEKGKSKKLKSVKELLGIT
                     IMERSSFEKNPIDFLEAKGYKEVKKDLIIKLPKYSLFELENGRKRMLASAGELQKGNEL
                     ALPSKYVNFLYLASHYEKLKGSPEDNEQKQLFVEQHKHYLDEIIEQISEFSKRVILADA
                     NLDKVLSAYNKHRDKPIREQAENIIHLFTLTNLGAPAAFKYFDTTIDRKRYTSTKEVLD
                     ATLIHQSITGLYETRIDLSQLGGDSRADPKKKRKV”
     CDS             complement(3362..3382)
                     /codon_start=1
                     /product=“nuclear localization signal of SV40 (simian virus
                     40) large T antigen”
                     /label=SV40 NLS
                     /translation=“PKKKRKV”
     CDS             complement(3395..7498)
                     /codon_start=1
                     /product=“Cas9 (Csn1) endonuclease from the Streptococcus
                     pyogenes Type II CRISPR/Cas system”
                     /label=Cas9
                     /note=“generates RNA-guided double strand breaks in DNA”
                     /translation=“MDKKYSIGLDIGTNSVGWAVITDEYKVPSKKFKVLGNTDRHSIKK
                     NLIGALLFDSGETAEATRLKRTARRRYTRRKNRICYLQEIFSNEMAKVDDSFFHRLEES
                     FLVEEDKKHERHPIFGNIVDEVAYHEKYPTIYHLRKKLVDSTDKADLRLIYLALAHMIK
                     FRGHFLIEGDLNPDNSDVDKLFIQLVQTYNQLFEENPINASGVDAKAILSARLSKSRRL
                     ENLIAQLPGEKKNGLFGNLIALSLGLTPNFKSNFDLAEDAKLQLSKDTYDDDLDNLLAQ
                     IGDQYADLFLAAKNLSDAILLSDILRVNTEITKAPLSASMIKRYDEHHQDLTLLKALVR
                     QQLPEKYKEIFFDQSKNGYAGYIDGGASQEEFYKFIKPILEKMDGTEELLVKLNREDLL
                     RKQRTFDNGSIPHQIHLGELHAILRRQEDFYPFLKDNREKIEKILTFRIPYYVGPLARG
                     NSRFAWMTRKSEETITPWNFEEVVDKGASAQSFIERMTNFDKNLPNEKVLPKHSLLYEY
                     FTVYNELTKVKYVTEGMRKPAFLSGEQKKAIVDLLFKTNRKVTVKQLKEDYFKKIECFD
                     SVEISGVEDRFNASLGTYHDLLKIIKDKDFLDNEENEDILEDIVLTLTLFEDREMIEER
                     LKTYAHLFDDKVMKQLKRRRYTGWGRLSRKLINGIRDKQSGKTILDFLKSDGFANRNFM
                     QLIHDDSLTFKEDIQKAQVSGQGDSLHEHIANLAGSPAIKKGILQTVKVVDELVKVMGR
                     HKPENIVIEMARENQTTQKGQKNSRERMKRIEEGIKELGSQILKEHPVENTQLQNEKLY
                     LYYLQNGRDMYVDQELDINRLSDYDVDHIVPQSFLKDDSIDNKVLTRSDKNRGKSDNVP
                     SEEVVKKMKNYWRQLLNAKLITQRKFDNLTKAERGGLSELDKAGFIKRQLVETRQITKH
                     VAQILDSRMNTKYDENDKLIREVKVITLKSKLVSDFRKDFQFYKVREINNYHHAHDAYL
                     NAVVGTALIKKYPKLESEFVYGDYKVYDVRKMIAKSEQEIGKATAKYFFYSNIMNFFKT
                     EITLANGEIRKRPLIETNGETGEIVWDKGRDFATVRKVLSMPQVNIVKKTEVQTGGFSK
                     ESILPKRNSDKLIARKKDWDPKKYGGFDSPTVAYSVLVVAKVEKGKSKKLKSVKELLGI
                     TIMERSSFEKNPIDFLEAKGYKEVKKDLIIKLPKYSLFELENGRKRMLASAGELQKGNE
                     LALPSKYVNFLYLASHYEKLKGSPEDNEQKQLFVEQHKHYLDEIIEQISEFSKRVILAD
                     ANLDKVLSAYNKHRDKPIREQAENIIHLFTLTNLGAPAAFKYFDTTIDRKRYTSTKEVL
                     DATLIHQSITGLYETRIDLSQLGGD”
     misc_feature    7496..7498
                     /label=alpha
                     /note=“alpha”
     sig_peptide     7496..7498
                     /label=alpha
     misc_feature    join(8499..8509,1..9)
                     /label=R3
{}
//
""".format((gene_i + str(guide_num_curr_int)), marker, genbank_seq)
    if OS == "W":
        output_file = directory + "\\{}{}_{}_{}.gb".format(gene_i, str(guide_num_curr_int), gene_gq, marker)
    if OS == "U":
        output_file = directory + "/{}{}_{}_{}.gb".format(gene_i, str(guide_num_curr_int), gene_gq, marker)
    r = open(output_file, 'w')
    r.write(genbank_full)
    r.close()
    print("R-vec file created.")

#Concatonates homology arms with DS sequence
#returns full DS ins seq
def DS_frag_seq_create(homology_arm_upstream, homology_arm_downstream):
    ds_seq = ("taagtaagtaaattgcttgaagctttaatttattttattaacataataataatac" +
    "aagcatgatatatttgtattttgttcgttaacattgatgttttcttcatttactgttattgtttgta" +
    "actttgatcgatttatcttttctactttactgtaatatggctggcgggtgagccttgaactccctgt" +
    "attactttaccttgctattacttaat")

    ds_full = homology_arm_upstream + ds_seq + homology_arm_downstream
    return ds_full

#input: primer start index, primer end index, primer label
def primer_create_gb(primer_start_ind, primer_end_ind, label):
    primer_gb = ("""     primer_bind     {}..{}
                     /label={}""".format(primer_start_ind, primer_end_ind, label))
    print(primer_gb)
#input: primer sequence
#output: melting temp in degrees C
def primer_tm_calc(primer):
    a_t = 0
    g_c = 0

    for bp in primer:
        if bp == "a" or bp == "t":
            a_t += 1
        elif bp =="g" or bp == "c":
            g_c += 1

    temp = 69.49 + (41*(g_c - 16.4) / (g_c + a_t))
    return temp

def ds_seq_to_gb_file(seq, gene_name, guide_num, output_dir):
    primer_template = "primer"
    ds_ins_full = """LOCUS       Exported                2540 bp DNA     circular SYN
DEFINITION  synthetic circular DNA
ACCESSION   .
VERSION     .
KEYWORDS    .
SOURCE      synthetic DNA construct
  ORGANISM  synthetic DNA construct
REFERENCE   1  (bases 1 to 2540)

FEATURES             Location/Qualifiers
     source          1..2540
                     /organism="synthetic DNA construct"
                     /mol_type="other DNA"
     misc_feature    1..40
                     /label=L1
     misc_feature    41..455
                     /label={0}_100bp Homology arm Death Star
     misc_feature    41..140
                     /label={1}_100BP_Upstream
     misc_feature    141..355
                     /label=DeathStar
     misc_feature    356..455
                     /label={2}_100BP_Downstream
     misc_feature    456..495
                     /label=L4
     promoter        496..915
                     /label=pTEF1
                     /note="TEF1 promoter"
     misc_feature    916..955
                     /label=L5
     terminator      916..948
                     /label=CYC1 transcription terminator
     misc_feature    949..988
                     /label=L6
     promoter        961..1028
                     /label=EM7 promoter
     promoter        963..1010
                     /label=EM7 promoter
                     /note="synthetic bacterial promoter "
     terminator      989..1261
                     /label=CYC1 transcription terminator
     terminator      1009..1256
                     /gene="S. cerevisiae CYC1"
                     /label=CYC1 terminator
                     /note="transcription terminator for CYC1"
     CDS             1029..1403
                     /codon_start=1
                     /gene="Sh ble from Streptoalloteichus hindustanus"
                     /product="antibiotic-binding protein"
                     /label=BleoR
                     /note="confers resistance to bleomycin, phleomycin, and
                     Zeocin(TM)"
                     /translation="MAKLTSAVPVLTARDVAGAVEFWTDRLGFSRDFVEDDFAGVVRDD
                     VTLFISAVQDQVVPDNTLAWVWVRGLDELYAEWSEVVSTNFRDASGPAMTEIGEQPWGR
                     EFALRDPAGNCVHFVAEEQD"
     CDS             1029..1403
                     /label=Zeo(R)
     rep_origin      complement(1272..1945)
                     /direction=LEFT
                     /label=pUC origin
     rep_origin      complement(1331..1919)
                     /direction=LEFT
                     /label=ori
                     /note="high-copy-number ColE1/pMB1/pBR322/pUC origin of
                     replication"
     terminator      1404..1448
                     /label=CYC1 transcription terminator
     misc_feature    1449..1488
                     /label=L6
     terminator      1489..1761
                     /label=CYC1 transcription terminator
     terminator      1509..1756
                     /gene="S. cerevisiae CYC1"
                     /label=CYC1 terminator
                     /note="transcription terminator for CYC1"
     rep_origin      complement(1772..2445)
                     /direction=LEFT
                     /label=pUC origin
     rep_origin      complement(1831..2419)
                     /direction=LEFT
                     /label=ori
                     /note="high-copy-number ColE1/pMB1/pBR322/pUC origin of
                     replication"
     promoter        2000
                     /label=AOX1 promoter
     misc_feature    2001..2040
                     /label=L8
     misc_feature    2501..2540
                     /label=L8

ORIGIN
        1 catactatca cgtcggcgac caccagtgag ttactagagc {3}actctg tactgagttct
	  ataaacg
      481 agccattgca tacgacccac acaccatagc ttcaaaatgt ttctactcct tttttactct
      541 tccagatttt ctcggactcc gcgcatcgcc gtaccacttc aaaacaccca agcacagcat
      601 actaaatttt ccctctttct tcctctaggg tgtcgttaat tacccgtact aaaggtttgg
      661 aaaagaaaaa agagaccgcc tcgtttcttt ttcttcgtcg aaaaaggcaa taaaaatttt
      721 tatcacgttt ctttttcttg aaattttttt ttttagtttt tttctctttc agtgacctcc
      781 attgatattt aagttaataa acggtcttca atttctcaag tttcagtttc atttttcttg
      841 ttctattaca acttttttta cttcttgttc attagaaaga aagcatagca atctaatcta
      901 agttttaatt acaaagaaag cgacccgagg ttctaaccgc cgactttggc ggaaagggcg
      961 gtgttgacaa ttaatcatcg gcatagtata tcggcatagt ataatacgac aaggtgagga
     1021 actaaaccat ggccaagttg accagtgccg ttccggtgct caccgcgcgc gacgtcgccg
     1081 gagcggtcga gttctggacc gaccggctcg ggttctcccg ggacttcgtg gaggacgact
     1141 tcgccggtgt ggtccgggac gacgtgaccc tgttcatcag cgcggtccag gaccaggtgg
     1201 tgccggacaa caccctggcc tgggtgtggg tgcgcggcct ggacgagctg tacgccgagt
     1261 ggtcggaggt cgtgtccacg aacttccggg acgcctccgg gccggccatg accgagatcg
     1321 gcgagcagcc gtgggggcgg gagttcgccc tgcgcgaccc ggccggcaac tgcgtgcact
     1381 tcgtggccga ggagcaggac tgacacgtcc gacggcggcc cacgggtccc aggcctcgga
     1441 gatccgtcgg tttcactcag gaagcagaca ctgattgaca cggtttagcc ccttttcctt
     1501 tgtcgatatc atgtaattag ttatgtcacg cttacattca cgccctcccc ccacatccgc
     1561 tctaaccgaa aaggaaggag ttagacaacc tgaagtctag gtccctattt atttttttat
     1621 agttatgtta gtattaagaa cgttatttat atttcaaatt tttctttttt ttctgtacag
     1681 acgcgtgtac gcatgtaaca ttatactgaa aaccttgctt gagaaggttt tgggacgctc
     1741 gaaggcttta atttgcaagc tggagaccaa catgtgagca aaaggccagc aaaaggccag
     1801 gaaccgtaaa aaggccgcgt tgctggcgtt tttccatagg ctccgccccc ctgacgagca
     1861 tcacaaaaat cgacgctcaa gtcagaggtg gcgaaacccg acaggactat aaagatacca
     1921 ggcgtttccc cctggaagct ccctcgtgcg ctctcctgtt ccgaccctgc cgcttaccgg
     1981 atacctgtcc gcctttctcc cttcgggaag cgtggcgctt tctcaatgct cacgctgtag
     2041 gtatctcagt tcggtgtagg tcgttcgctc caagctgggc tgtgtgcacg aaccccccgt
     2101 tcagcccgac cgctgcgcct tatccggtaa ctatcgtctt gagtccaacc cggtaagaca
     2161 cgacttatcg ccactggcag cagccactgg taacaggatt agcagagcga ggtatgtagg
     2221 cggtgctaca gagttcttga agtggtggcc taactacggc tacactagaa ggacagtatt
     2281 tggtatctgc gctctgctga agccagttac cttcggaaaa agagttggta gctcttgatc
     2341 cggcaaacaa accaccgctg gtagcggtgg tttttttgtt tgcaagcagc agattacgcg
     2401 cagaaaaaaa ggatctcaag aagatccttt gatcttttct acggggtctg acgctcagtg
     2461 gaacgaaaac tcacgttaag ggattttggt catgagatca gacccgatga actacagaac
     2521 actgcaagaa tctctacctg
//
""".format(gene_name, gene_name, gene_name, seq)

    if OS == "W":
        output_file = output_dir + "\\DS_ins_{}-{}.gb".format(gene_name, str(guide_num))
    if OS == "U":
        output_file = output_dir + "/DS_ins_{}-{}.gb".format(gene_name, str(guide_num))
    r = open(output_file, 'w')
    r.write(ds_ins_full)
    r.close()
    print("DS insert file created.")

#input: Gene name(str), guide_num(int) Deathstart insert seq(str),
    #primer label current(str), primer # current(int)
#output: primer_label[(str)], primer_seq[(str)],
    #primer_description[(str)], new primer # current(int), ds_gb_file, updated primer num (int)
def DS_gb_create(gene_name, guide_num, ds_seq, primer_label, primer_num_curr, output_dir):
    print("Continuing primer list from {}{}".format(primer_label, str(primer_num_curr)))
    print(ds_seq)
    primer_num_curr += 1
    output = []
    primer_label_arr = []
    primer_seq_arr = []
    primer_desc_arr = []
    primer_num = primer_num_curr
    ds_primer_fwd_base = "taagtaagtaaattgcttgaagctttaatt"
    ds_primer_rev_base_fwd = "attaagtaatagcaaggtaaagtaatacag"
    #reverse primer sequence to match complement read in line with fwd seq
    ds_primer_rev_base = ds_primer_rev_base_fwd[::-1]
    #create temporary complement
    ds_seq_comp = ""
    for bp in ds_seq:
        if bp == "a":
            ds_seq_comp += "t"
        elif bp == "t":
            ds_seq_comp += "a"
        elif bp == "g":
            ds_seq_comp += "c"
        elif bp == "c":
            ds_seq_comp += "g"
    print("DS complement is:\n")
    print(ds_seq_comp[::-1])

    ds_seq_comp_rev = ds_seq_comp[::-1]
    primer_fwd_index = ds_seq.find(ds_primer_fwd_base)
    primer_rev_index = ds_seq_comp_rev.find(ds_primer_rev_base_fwd)
    print("Found DS primer fwd index at {}".format(primer_fwd_index))
    print("Found DS primer rev index at {}".format(primer_rev_index))

    primer_fwd_overhang = ""
    primer_rev_overhang = ""

    #generate fwd primer homology overhang (30bp)
    for index, bp in enumerate(ds_seq):
        if (index >= primer_fwd_index - 30) and (index < primer_fwd_index):
            primer_fwd_overhang += bp

    #generate rev primer homology overhang (30bp)
    for index, bp in enumerate(ds_seq_comp_rev):
        if (index >= primer_rev_index - 30) and (index < primer_rev_index):
            primer_rev_overhang += bp

    primer_fwd_full = primer_fwd_overhang + ds_primer_fwd_base
    #append primer data to arrays
    primer_label_arr.append(primer_label + str(primer_num_curr))
    primer_seq_arr.append(primer_fwd_full)
    primer_desc_arr.append("Deathstar_ins_{}-{}_30bp_fwd".format(gene_name, guide_num))
    primer_num_curr += 1 #iterate

    primer_rev_full = primer_rev_overhang + ds_primer_rev_base_fwd
    primer_label_arr.append(primer_label + str(primer_num_curr))
    primer_seq_arr.append(primer_rev_full)
    primer_desc_arr.append("Deathstar_ins_{}-{}_30bp_rev".format(gene_name, guide_num))
    primer_num_curr += 1 #iterate

    print("DS primer fwd with overhang is: " + primer_fwd_full)
    print("DS primer rev with overhang is: " + primer_rev_full)

    #Now make primers for sequence arms too
    #primer_tm_calc(primer)
    upstream_fwd = ""
    downstream_rev = ""
    for index, bp in enumerate(ds_seq):
        if (index >= 0) and (index < 20):
            upstream_fwd += bp
        if (index >= 20):
            tm = primer_tm_calc(upstream_fwd)
            print("Calculated melting temp for {} is {}: ".format(primer_label + str(primer_num_curr), tm))
            if (tm > 56):
                break;
            else: upstream_fwd += bp
    primer_label_arr.append(primer_label + str(primer_num_curr))
    primer_seq_arr.append(upstream_fwd)
    primer_desc_arr.append("{}_DS_ins_full_fwd".format(gene_name))
    print("Primer {} stored with sequence {}".format(primer_label + str(primer_num_curr), upstream_fwd))
    primer_num_curr += 1

    for index, bp in enumerate(ds_seq_comp_rev):
        if (index >= 0) and (index < 20):
            downstream_rev += bp
        if (index >= 20):
            tm = primer_tm_calc(downstream_rev)
            print("Calculated melting temp for {} is {}: ".format(primer_label + str(primer_num_curr), tm))
            if (tm > 56):
                break;
            else: downstream_rev += bp
    primer_label_arr.append(primer_label + str(primer_num_curr))
    primer_seq_arr.append(downstream_rev)
    primer_desc_arr.append("{}_DS_ins_full_rev".format(gene_name))
    print("Primer {} stored with sequence {}".format(primer_label + str(primer_num_curr), downstream_rev))
    primer_num_curr += 1

    #Write gb file
    ds_seq_to_gb_file(ds_seq, gene_name, guide_num, output_dir)
    #ds_seq_to_gb_file(ds_seq, gene_name, guide_num)
    #seq_to_gb_file(ds_ins_seq, primer_label_arr, primer_seq_arr, primer_desc_arr)

    #return output[primer_label_arr, primer_seq_arr, primer_desc_arr, primer_num_curr]
    output.append(primer_label_arr)
    output.append(primer_seq_arr)
    output.append(primer_desc_arr)
    output.append(primer_num_curr)
    return output

def locus_seq_to_gb_file(seq, gene_name, output_dir):
    seq_len = len(seq) + 1
    locus_ins_full = """LOCUS       Exported                2540 bp DNA     linear
DEFINITION  natural linear DNA
ACCESSION   .
VERSION     .
KEYWORDS    .
SOURCE      synthetic DNA construct
  ORGANISM  synthetic DNA construct
REFERENCE   1  (bases 1 to 2540)

FEATURES             Location/Qualifiers
     source          1..{0}
                     /organism="synthetic DNA construct"
                     /mol_type="other DNA"
     misc_feature    101..{1}
                     /label={2}


ORIGIN
        1 {3}
//
""".format(seq_len, seq_len - 100, gene_name, seq)
    if OS == "W":
        output_file = output_dir + "\\{}_Locus.gb".format(gene_name)
    if OS == "U":
        output_file = output_dir + "/{}_Locus.gb".format(gene_name)
    r = open(output_file, 'w')
    r.write(locus_ins_full)
    r.close()
    print("Locus insert file created.")


#****menu prompts****
OS = input("Unix or Windows OS? (U/W) ")
while not (OS == 'U' or OS == 'W'):
    print("Invalid Response.")
    OS = input("Unix or Windows OS? (U/W) ")

#obtain the active directory
###C:\Users\Tim\Desktop\Python_Project_Files
active_dir = input("Please enter the directory for the Python_Project_Files folder: ")
while not os.path.exists(active_dir):
    if not (active_dir == "E" or active_dir == "e"):
        active_dir = input("""The directory entered does not exist,
            please re-enter the working directory or enter "E" to exit the program: """)
    else: exit()

if (os.path.exists(active_dir)):
    print("Directory found successfully")

primer_num_curr = input("""For primer creation, please enter the number to start from (INTEGER ONLY): """)
primer_var_is_int = False
while (primer_var_is_int == False):
    try:
        primer_num_curr_int = int(primer_num_curr)
        if isinstance(primer_num_curr_int, int):
            primer_var_is_int = True
    except ValueError:
            print("Entered value was not an integer. Please try again.")
            primer_num_curr = input("""For primer creation, please enter the number to start from (INTEGER ONLY): """)

primer_annotation = input("""For primer creation, please enter any prefixes, initials,
or other annotation you want before each primer number (hit enter if none): """)

#primer data storage
primer_label_total = []
primer_seq_total = []
primer_desc_total = []

#guide_data_storage
guide_label_total = []
guide_seq_total = []
guide_desc_total = []

#Windows
if (OS == 'W'):
    input_folder = (active_dir + "\input_files")
    print("Given folder directory: " + input_folder)
    while not os.path.exists(input_folder):
        if not (active_dir == "E" or active_dir == "e"):
            active_dir = input("""The input_folder could not be found in the provided directory
            please re-enter the working directory or enter "E" to exit the program: """)
            input_folder = (active_dir + "\input_files")
        else: exit()
    if (os.path.exists(input_folder)):
        print("Folder found successfully")

    chr_1 = input_folder + "\chr1.csv"
    chr_2 = input_folder + "\chr2.csv"
    chr_3 = input_folder + "\chr3.csv"
    chr_4 = input_folder + "\chr4.csv"
    guide_list = input_folder + "\KO_guide_List.csv"
    input_ss = input_folder + "\Python_Project_Input.csv"

    #Create output folder
    if not (os.path.exists(active_dir + "\\output_files")):
            print("Creating output_files folder. Created files will be stored here.")
            os.mkdir(active_dir + "\\output_files")
            output_folder = active_dir + "\\output_files"
    else:
            print("output_files folder found. Created files will be stored here.")
            output_folder = active_dir + "\\output_files"

#Unix (iOS or Linux)
if (OS == 'U'):
    input_folder = (active_dir + "/input_files")
    print("Given folder directory: " + input_folder)
    while not os.path.exists(input_folder):
        if not (active_dir == "E" or active_dir == "e"):
            active_dir = input("""The input_folder could not be found in the provided directory
            please re-enter the working directory or enter "E" to exit the program: """)
            input_folder = (active_dir + "\input_files")
        else: exit()
    if (os.path.exists(input_folder)):
        print("Folder found successfully")

    chr_1 = input_folder + "/chr1.csv"
    chr_2 = input_folder + "/chr2.csv"
    chr_3 = input_folder + "/chr3.csv"
    chr_4 = input_folder + "/chr4.csv"
    guide_list = input_folder + "/KO_guide_List.csv"
    input_ss = input_folder + "/Python_Project_Input.csv"

    #Create output folder
    if not (os.path.exists(active_dir + "/output_files")):
            print("Creating output_files folder. Created files will be stored here.")
            os.mkdir(active_dir + "/output_files")
            output_folder = active_dir + "/output_files"
    else:
            print("output_files folder found. Created files will be stored here.")
            output_folder = active_dir + "/output_files"
#find the appropriate folders
if (os.path.exists(chr_1) and os.path.exists(chr_2)
    and os.path.exists(chr_3) and os.path.exists(chr_4)):
    print("All input files located. Proceeding to parse Python_Project_Input.csv")
else:
    print("""The files needed to run the program are not present.
    The "input_files" folder should contain:
        chr1.csv,
        chr2.csv,
        chr3.csv,
        chr4.csv,
        KO_guide_List.csv,
        Python_Project_Input.csv
    The program will now close.""")
    exit()

#get input data from Python_Project_Input.csv

open(input_ss, "rt")
with open(input_ss, "rt") as i:
    reader = csv.DictReader(i)
    target_gene = [row["target_gene"]for row in reader]
    i.close()


with open(input_ss, "rt") as i:
    reader = csv.DictReader(i)
    vec_marker = [row["r-vec_marker"]for row in reader]
    i.close()

#This for loop will ocmprise the rest of the program
#Every action will be performed for every gene in this target_gene array

for iteration, i in enumerate(target_gene):
    guide_num_curr_int = 1
    while (len(i)<4):
        i = "0" + i
    gene_i = "Kpha" + i
    vec_marker_i = vec_marker[iteration]
    print("Gene {}:\t{} with {} marker.".format((iteration + 1), gene_i, vec_marker[iteration]))

    int_i = int(i)

    if ((int_i >= 1355) and (int_i <= 2978)):

        gene_i_chr = chr_1
        try:
            gene_coord_output = chr_search(gene_i, gene_i_chr)
        except:
            print("Gene {} is not annotated in the genome, Proceeding to next gene.".format(gene_i))
            continue

        print("Gene {} was found in Chromosome 1. Beginning file generation".format(gene_i))
        #parse chr1.csv for gene_id


    elif ((int_i >= 31) and (int_i <= 1353)):
        gene_i_chr = chr_2
        try:
            gene_coord_output = chr_search(gene_i, gene_i_chr)
        except:
            print("Gene {} is not annotated in the genome, Proceeding to next gene.".format(gene_i))
            continue

        print("Gene {} was found in Chromosome 2. Beginning file generation".format(gene_i))
    elif ((int_i >= 3018) and (int_i <= 4303)):
        gene_i_chr = chr_3
        try:
            gene_coord_output = chr_search(gene_i, gene_i_chr)
        except:
            print("Gene {} is not annotated in the genome, Proceeding to next gene.".format(gene_i))
            continue

        print("Gene {} was found in Chromosome 3. Beginning file generation".format(gene_i))

    elif ((int_i >= 4305) and (int_i <= 5290)):
        gene_i_chr = chr_4
        try:
            gene_coord_output = chr_search(gene_i, gene_i_chr)
        except:
            print("Gene {} is not annotated in the genome, Proceeding to next gene.".format(gene_i))
            continue

        print("Gene {} was found in Chromosome 4. Beginning file generation".format(gene_i))
    print(gene_coord_output)

    for index, var in enumerate(gene_coord_output):
        if index == 0:
            gene_i_start = var
        elif index == 1:
            gene_i_end = var
        elif index == 2:
            gene_i_complement = var

    print(gene_i + " starts at " + gene_i_start)
    print(gene_i + " ends at " + gene_i_end)
    print("Sequence is complement: " + str(gene_i_complement))

    gene_i_start_int = int(gene_i_start)
    gene_i_end_int = int(gene_i_end)

    #gene string of gene sequence

    ##loci will have + 100bp homology arms in the event that guide is very near the beginning
    locus_array = locus_seq_string(gene_i_chr, gene_i_start_int - 100, gene_i_end_int + 100, gene_i_complement, primer_annotation, primer_num_curr_int)

    for index, var in enumerate(locus_array):
        if index == 0:
            locus_seq_fwd = var
        elif index == 1:
            locus_seq_complement = var
        elif index == 2:
            primer_num_curr_int = var
        elif index == 3:
            for label in var:
                primer_label_total.append(label)
        elif index == 4:
            for seq in var:
                primer_seq_total.append(seq)
        elif index == 5:
            for desc in var:
                primer_desc_total.append(desc)


    print(locus_seq_fwd)
    print(locus_seq_complement)

    #if no output folder, create one
    #in output folder, save string as locus file
    if OS == "W":
        if not (os.path.exists(active_dir + "\\output_files\\{}_{}".format(gene_i, vec_marker_i))):
            output_dir = active_dir + "\\output_files\\{}_{}".format(gene_i, vec_marker_i)
            os.mkdir(output_dir)
        else: output_dir = active_dir + "\\output_files\\{}_{}".format(gene_i, vec_marker_i)

    elif OS == "U":
        if not (os.path.exists(active_dir + "/output_files/{}_{}".format(gene_i, vec_marker_i))):
            output_dir = active_dir + "/output_files/{}_{}".format(gene_i, vec_marker_i)
            os.mkdir(output_dir)
        else: output_dir = active_dir + "/output_files/{}_{}".format(gene_i, vec_marker_i)

    #Write Locus to gb file
    locus_seq_to_gb_file(locus_seq_fwd, gene_i, output_dir)

    #Parse database ss for guide sequences
    if OS == "W":
        guide_ss = input_folder +"\\KO_Guide_List.csv"
    elif OS == "U":
        guide_ss = input_folder +"/KO_Guide_List.csv"
    gene_gq = "GQ67_0" + i
    gene_i_guides = gene_get_gRNA(guide_ss, gene_gq)
    guide_count = 1


    #Create CRISPR R-vec plasmid based on guide sequence
    for guide in gene_i_guides:
        R_vec_create(guide, vec_marker_i, output_dir)
        print("Now creating R-Vector {} containing {}{} for {}".format(str(guide_count), gene_i, str(guide_num_curr_int), gene_i))

        #add guide data to global list
        guide_label_total.append(gene_i + str(guide_num_curr_int))
        guide_seq_total.append(guide)
        guide_desc_total.append("{}-{}_{}".format(gene_i, str(guide_count),  vec_marker_i))

        ##Find guide seqences in forward or complement string
        #convert to lowercase for parsing, case sensitive
        guide_lc = ""
        guide_len = 0
        for character in guide:
            if character == "A":
                guide_lc += "a"
            elif character == "G":
                guide_lc += "g"
            elif character == "C":
                guide_lc += "c"
            elif character == "T":
                guide_lc += "t"
            guide_len += 1
        print("guide_lc is: {}".format(guide_lc))
        guide_rev = guide_lc[::-1]

        guide_found_fwd = locus_seq_fwd.find(guide_lc)
        guide_found_complement = locus_seq_complement.find(guide_rev)
        if guide_found_fwd == -1:
            print("The guide fwd {} was not found in the forward locus sequence.".format(guide_lc))
        else:
            print("The guide fwd {} was found at index {}.".format(guide_lc, guide_found_fwd))
            guide_seq_start = guide_found_fwd

        if guide_found_complement == -1:
            print("The guide complement {} was not found in the complementary locus sequence.".format(guide_rev))
        else:
            print("The guide complement {} was found at index {}.".format(guide_rev, guide_found_complement))
            guide_seq_start = guide_found_complement

        #Store 100bp homology arm sequences
            #upsstream and downstream are relative to exon reading frame
        homology_arm_upstream = ""
        homology_arm_downstream = ""
        if ((not guide_found_fwd == -1) and (guide_found_complement == -1)):
            for index, bp in enumerate(locus_seq_fwd):
                if ((index >= (guide_seq_start - 100)) and (index < guide_seq_start)):
                    homology_arm_upstream += bp
                elif ((index >= (guide_seq_start + guide_len + 3)) and
                      (index < guide_seq_start + guide_len + 103)):
                    homology_arm_downstream += bp

        elif ((not guide_found_complement == -1) and (guide_found_fwd == -1)):
            for index, bp in enumerate(locus_seq_fwd):
                if ((index >= (guide_seq_start - 103)) and (index < guide_seq_start - 3)):
                    homology_arm_upstream += bp
                elif ((index >= (guide_seq_start + guide_len)) and (index < guide_seq_start + guide_len + 100)):
                    homology_arm_downstream += bp
        else: print("Error in creating DS ins for guide {}".format(guide))
        print("Upstream arm is:\n " + homology_arm_upstream)
        print("Downstream arm is:\n " + homology_arm_downstream)

        #Create deathstar string based on FWD read only, or DS won't be read
        ds_ins = DS_frag_seq_create(homology_arm_upstream, homology_arm_downstream)

        ds_output = DS_gb_create(gene_i, guide_num_curr_int, ds_ins, primer_annotation, primer_num_curr_int, output_dir)

        for index, var in enumerate(ds_output):
            if index == 0:
                for label in var:
                    primer_label_total.append(label)
            elif index == 1:
                for seq in var:
                    primer_seq_total.append(seq)
            elif index == 2:
                for desc in var:
                    primer_desc_total.append(desc)
            elif index == 3:
                primer_num_curr_int = var

        #increment_guide_num
        guide_num_curr_int += 1
        guide_count += 1
    #Write locus seq to Genbank file in output folder

    #Output all primers and inserts
    #Add-on: Generate DS geneblock to insert in to L-vector for subcloning, primers, etc
for index, i in enumerate(guide_label_total):
    print("Guide {} on list is: ".format(str(index+1)) + guide_label_total[index])
    print(guide_seq_total[index])
    print(guide_desc_total[index])

primer_output = "Primer,Sequence,Description\n"
for index, primer in enumerate(primer_label_total):
    i = index
    primer_output += "{},{},{}\n".format(primer_label_total[i], primer_seq_total[i], primer_desc_total[i])
if OS == "W":
    output_file = output_folder + "\\Primer_List.csv"
if OS == "U":
    output_file = output_folder + "/Primer_List.csv"
r = open(output_file, 'w')
r.write(primer_output)
r.close()
print("Primer List Created")

guide_output = "Guide,Sequence,Description,R-vec_Ins\n"
guide_ins_u = "TCAATTCCCCGTCGCGGAGC"
guide_ins_d = "GTTTTAGAGCTAGAAATAGC"
for index, guide in enumerate(guide_label_total):
    i = index
    guide_output += "{},{},{},{}\n".format(guide_label_total[i], guide_seq_total[i], guide_desc_total[i], guide_ins_u + guide_seq_total[i] + guide_ins_d)
if OS == "W":
    output_file = output_folder + "\\Guide_List.csv"
if OS == "U":
    output_file = output_folder + "/Guide_List.csv"
r = open(output_file, 'w')
r.write(guide_output)
r.close()
print("Guide List Created")
