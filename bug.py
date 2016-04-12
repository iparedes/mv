__author__ = 'nacho'

# Types of memory cells
FREE=0 # Free Cell
TERM=1 # Terminal cell, stores a value
NTER=2 # Non terminal cell, stores car,cdr


MAX_MEM=1000



class bug:
    def __init__(self):
        self._memory=[None]*(MAX_MEM+1)
        self._freelist=range(1,MAX_MEM+1)


        self._registers={}

        # 'S': General Stack
        self._registers['S']=self._new()
        self._set_nt(self._registers['S'],0,0)



    def _new(self):
        """allocates an unused memory address

        Returns:
        An unused memory address (int)

        """
        try:
            return self._freelist.pop(0)
        except IndexError, e:
            return 0

    def _set(self,address,value):
        """sets a terminal cell

        Keyword arguments:
        address -- the memory address to set
        value -- the value to put in the address (an integer)
        """

        # Only sets if address is valid
        if (address>0) and (address<=MAX_MEM):
            self._memory[address]=[TERM,value]

    def _set_nt(self,address,car,cdr):
        """sets a non terminal cell

        Keyword arguments:
        address -- the memory address to set
        car -- the head of the list
        cdr -- the tail of the list
        """
        # Only sets if address is valid
        if (address>0) and (address<=MAX_MEM):
            self._memory[address]=[NTER,car,cdr]

    def _push(self,stack,value):
        """Pushes value into the stack

        Keyword arguments:
        stack -- the name of the stack as it is in the registers list
        value -- the value to stack (an integer)
        """
        try:
            n=self._new()
            self._set(n,value)
            m=self._new()
            self._set_nt(m,n,self._registers[stack])
            self._registers[stack]=m
        except KeyError,e:
            pass


    def _pop(self,stack):
        """Pops a value from the stack
        If the stack is empty returns 0

        Keyword arguments:
        stack -- the name of the stack as it is in the registers list
        """
        a=self._registers[stack]
        car=self._memory[a][1]
        cdr=self._memory[a][2]
        if car==0:
            return 0
        else:
            valor=self._memory[car][1]
            self._registers[stack]=cdr
            self._free(car)
            self._free(a)
            return valor


    def _free(self,address):
        """Frees a memory address
        """
        if address!=0:
            self._memory[address][0]=FREE
            self._freelist.append(address)

    def _is_empty(self,l):
        """Returns TRUE if the list/stack is empty
        Keyword arguments:
        l -- a memory address which is the head of the list/stack

        """
        return self._memory[l][0]==NTER and self._memory[l][1]==0 and self._memory[l][2]==0

    def _is_terminal(self,address):
        """Returns TRUE if the address is a terminal cell

        Keyword arguments:
        address -- a memory address

        """
        return self._memory[address][0]==TERM




    def _dump_list(self,a):
        """Print the list

        Keyword arguments:
        a -- a memory address as the head of the list
        """

        try:

            while a!=0:
                tipo=self._memory[a][0]
                if tipo==TERM:
                    print '(T,',self._memory[a][1],')'
                    return
                elif tipo==NTER:
                    self._dump_list(self._memory[a][1])
                    self._dump_list(self._memory[a][2])
                    return
        except KeyError,e:
            pass


