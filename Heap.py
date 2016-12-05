

class Heapsort:

    def parentindexforbaseone(heap, rootindex):
        #find the parent index
        #for base one
        return rootindex //2

    def leftchildforbase1(heap, rootindex):
        #find the index of left child
        if rootindex*2 >= len(heap):
            return -1
        return rootindex*2

    def rightchildforbase1(heap, rootindex):
        #find the index of right child
        if rootindex*2 + 1 >= len(heap):
            return -1
        return rootindex*2 + 1


    def HfixUp(heapn,heaps, index):
        #fix up the heap after added
        k = index
        if heapn[k] > heapn[k//2]:
            return
        else:
            if k == 1:
                return
            a = heapn[k]
            heapn[k] = heapn[k//2]
            heapn[k//2] = a
            b = heaps[k]
            heaps[k] = heaps[k//2]
            heaps[k//2] = b

            Heapsort.HfixUp(heapn,heaps,k//2)

    def HheapAdd(heapn,heaps, root, word):
        #add to the heap
        heapn += [root]
        heaps += [word]

        Heapsort.HfixUp(heapn,heaps,len(heapn)-1)

    def lfixdown(heapn,heaps, rootindex):
        #fix down the bottom heap
        loc = rootindex
        lc = Heapsort.leftchildforbase1(heapn, loc)
        rc = Heapsort.rightchildforbase1(heapn, loc)
        a = heapn[loc]
        b = heaps[loc]
        if lc == -1 and rc == -1:
            return
        elif lc == -1:
            if heapn[loc] > heapn[rc]:
                heapn[loc] = heapn[rc]
                heapn[rc] = a
                heaps[loc] = heaps[rc]
                heaps[rc] = b
                Heapsort.lfixdown(heapn,heaps, rc)
        elif rc == -1:
            if heapn[loc] > heapn[lc]:
                heapn[loc] = heapn[lc]
                heapn[lc] = a
                heaps[loc] = heaps[rc]
                heaps[rc] = b
                Heapsort.lfixdown(heapn,heaps, lc)
        else:
            alist = [heapn[lc],heapn[rc]]
            way = [lc,rc][alist.index(min(alist))]
            if heapn[way] < heapn[loc]:
                heapn[loc] = heapn[way]
                heapn[way] = a
                heaps[loc] = heaps[way]
                heaps[way] = b
                Heapsort.lfixdown(heapn,heaps, way)

    def hfixdown(heapn,heaps, rootindex):
        #fix down the top heap
        loc = rootindex
        lc = Heapsort.leftchildforbase1(heapn, loc)
        rc = Heapsort.rightchildforbase1(heapn, loc)
        a = heapn[loc]
        b = heaps[loc]
        if lc == -1 and rc == -1:
            return
        elif lc == -1:
            if heapn[loc] < heapn[rc]:
                heapn[loc] = heapn[rc]
                heapn[rc] = a
                heaps[loc] = heaps[rc]
                heaps[rc] = b
                hfixdown(heapn,heaps, rc)
        elif rc == -1:
            if heapn[loc] < heapn[lc]:
                heapn[loc] = heapn[lc]
                heapn[lc] = a
                heaps[loc] = heaps[rc]
                heaps[rc] = b
                Heapsort.hfixdown(heapn,heaps, lc)
        else:
            alist = [heapn[lc],heapn[rc]]
            way = [lc,rc][alist.index(max(alist))]
            if heapn[way] > heapn[loc]:
                heapn[loc] = heapn[way]
                heapn[way] = a
                heaps[loc] = heaps[way]
                heaps[way] = b
                Heapsort.hfixdown(heapn,heaps, way)

    def LfixUp(heapn,heaps, index):
        #fix up the bottom heap
        #for base 1
        k = index
        if heapn[k] < heapn[k//2]:
            return
        else:
            if k == 1:
                return
            a = heapn[k]
            heapn[k] = heapn[k//2]
            heapn[k//2] = a
            b = heaps[k]
            heaps[k] = heaps[k//2]
            heaps[k//2] = b

            Heapsort.LfixUp(heapn,heaps,index//2)

    def LheapAdd(heapn,heaps, root, word):
        #add to the bottom heap
        heapn += [root]
        heaps += [word]
        Heapsort.LfixUp(heapn,heaps,len(heapn)-1)
