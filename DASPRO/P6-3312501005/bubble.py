FUNCTION BubbleSort(Data: list/array)
    #Dapatkan panjang (jumlah elemen) dari list A
    n = length(Data)  
    FOR i = 0 TO n - 1
        #Inisialisasi variabel untuk melacak apakah terjadi pertukaran pada iterasi dalam
        swapped = false

        FOR j = 0 TO n - i - 2
            #Bandingkan dua elemen yg bersebelahan
            IF A[j] > A[j + 1] THEN 
                #Jika elemen sebelumnya lebih besar, tukarkan posisinya
                swap A[j] and A[j + 1]  
                #Menandakan bahwa pertukaran telah dilakukan pada iterasi ini
                swapped = true  
	    ENDIF
	ENDFOR
        IF swapped = false THEN
 	    #Jika tidak ada pertukaranlagi, maka data sudah terurut dan algoritma berhenti
             break  
        ENDIF
   ENFOR
ENDFUNCTION