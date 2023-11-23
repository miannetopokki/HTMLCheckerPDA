import os
class PDA:
    def __init__(self, states, input_alphabet, stack_alphabet, transition, start_state, initial_stack_symbol):
        self.states = states
        self.input_alphabet = input_alphabet
        self.stack_alphabet = stack_alphabet
        self.transition = transition
        self.start_state = start_state
        self.current_state = start_state
        self.initial_stack_symbol = initial_stack_symbol
        self.stack = [initial_stack_symbol]

    def is_accepted(self):
        return not self.stack
    def process_input(self, input_string):

       
        #MULAI LOOPING
        for symbol in input_string:
            if ((self.current_state, symbol, self.stack[-1]) in self.transition and self.current_state in self.states):
                next_state, pop_symbol, push_symbols = self.transition[(self.current_state, symbol, self.stack[-1])]

                # Pindah ke state berikutnya
                self.current_state = next_state

                # Pop simbol dari stack

                if len(pop_symbol) >= 1 and pop_symbol != 'ε':
                    for symb in pop_symbol:
                        popped = self.stack.pop()
                        if popped != pop_symbol:
                            print(f"Error: Expected '{pop_symbol}' on top of stack, but got '{popped}'.")
                            return False
                # Push simbol-simbol ke stack
                if push_symbols != 'ε':
                    self.stack.extend(push_symbols)



                # Print stack setiap kali berubah
                print(f"Current State: {self.current_state}")
                print(f"({self.current_state}, {symbol}, {self.stack[-1]}).")
                print(self.stack)
            else:
                if (self.current_state != 'qpetikbody' and self.current_state != 'qpetikhead'and self.current_state != 'qpetikhtml'
                    and self.current_state != 'qpetiktitle' and self.current_state != 'qpetiklinkhead' and self.current_state != 'qkutiplinkhead'
                    and self.current_state != 'qdiv'):   #Handler ignorance
                    print(f"Error: No transition for ({self.current_state}, {symbol}, {self.stack[-1]}).")
                    return False
                


        #TERAKHIR BANGET
        popped = self.stack.pop()
        if(popped != initial_stack_symbol):
            return False
        print(self.stack)
        return self.is_accepted()

# Contoh penggunaan
states = {'q0','qcek','qhead','endhtml','qatrhtml','qclasshtml','qpetikhtml','qidhtml','qstylehtml'
          ,'qatrbody','qclassbody','qpetikbody','qstylebody','qidbody','qbody','endbody','qcekbody',
          'qatrhead','qclasshead','qpetikhead','qidhead','qstylehead,','qcekhead','endhead',
          'qtitle','qatrtitle','endtitle','qclasstitle','qstyletitle','qidtitle','qpetiktitle'
          ,'qlinkhead','qatrlinkhead','qkutiplinkhead','qclasslinkhead','qstylelinkhead','qidlinkhead','qhreflinkhead','qpetiklinkhead',
          'qscript','qatrscript','qpetikscript','qclassscript','qidscript','qstylescript','endscript','qsrcscript',
          'qdiv','qatrdiv','enddiv','qpetikdiv','qclassdiv','qiddiv','qstylediv',
          'qh','endh','qatrh','qclassh','qidh','qpetikh','qstyleh',
          'qp','qatrp','endp','qclassp','qidp','qpetikp','qstylep'} 
input_alphabet = {'<','h','t','m','l','>','/'}
stack_alphabet = {'Z', '1'}
transition = {
            
           
            #==============================HTML==============================
            ('q0', '<', 'Z'): ('q0', 'ε', '<'),
            ('q0', 'h', '<'): ('q0', 'ε', 'h'),
            ('q0', 't', 'h'): ('q0', 'ε', 't'),
            ('q0', 'm', 't'): ('q0', 'ε', 'm'),
            ('q0', 'l', 'm'): ('q0', 'ε', 'l'),
            ('q0','>','l') : ('qcek' ,'ε','X>'),
            ('q0',' ','l'): ('qatrhtml','ε','X'),
            ('qatrhtml',' ','X') : ('qatrhtml' , 'ε','ε'),
            ('qatrhtml','>','X'): ('qcek','ε','>'),


            ('endbody', '<', '>'): ('endhtml', '>', 'ε'),
            ('endhtml', '/', 'X'): ('endhtml', 'X', 'ε'),
            ('endhtml', 'h', 'l'): ('endhtml', 'l', 'ε'),
            ('endhtml', 't', 'm'): ('endhtml', 'm', 'ε'),
            ('endhtml', 'm', 't'): ('endhtml', 't', 'ε'),
            ('endhtml', 'l', 'h'): ('endhtml', 'h', 'ε'),
            ('endhtml', '>', '<'): ('qhtml', '<', 'ε'),
            ('qhtml', 'Z', 'ε'): ('qhtml', 'ε', 'ε'),

            #Q Attribute HTML
            ('qatrhtml','c','X') : ('qclasshtml','ε', 'c'),
            ('qclasshtml','l','c') : ('qclasshtml','ε','l'),
            ('qclasshtml','a','l') : ('qclasshtml','ε','a'),
            ('qclasshtml','s','a') : ('qclasshtml','a','ε'),
            ('qclasshtml','s','l') : ('qclasshtml','l','ε'),
            ('qclasshtml','=','c') : ('qclasshtml','c','ε'),
            ('qclasshtml','"','X') : ('qpetikhtml','ε','"'),
            ('qpetikhtml','"','"') : ('qatrhtml' , '"','ε'),

            ('qatrhtml','s','X') : ('qstylehtml','ε', 's'),
            ('qstylehtml','t','s') : ('qstylehtml','ε','t'),
            ('qstylehtml','y','t') : ('qstylehtml','ε','y'),
            ('qstylehtml','l','y') : ('qstylehtml','y','ε'),
            ('qstylehtml','e','t') : ('qstylehtml','t','ε'),
            ('qstylehtml','=','s') : ('qstylehtml','s','ε'),
            ('qstylehtml','"','X') : ('qpetikhtml','ε','"'),
            ('qpetikhtml','"','"') : ('qatrhtml' , '"','ε'),

            ('qatrhtml','i','X') : ('qidhtml','ε', 'i'),
            ('qidhtml','d','i') : ('qidhtml','i','ε'),
            ('qidhtml','=','X') : ('qidhtml','ε','ε'),
            ('qidhtml','"','X') : ('qpetikhtml','ε','"'),
            ('qpetikhtml','"','"') : ('qatrhtml' , '"','ε'),


            #==============================BODY==============================
          
            ('qcek',' ','>'):('qcek','ε','ε'),
            ('qcek', '<', '>'): ('qcek', 'ε', '<'),
            ('qcek', 'b', '<'): ('qbody', 'ε', 'b'),
            ('qbody', 'o', 'b'): ('qbody', 'ε', 'o'),
            ('qbody', 'd', 'o'): ('qbody', 'ε', 'd'),
            ('qbody', 'y', 'd'): ('qbody', 'ε', 'y'),
            ('qbody', '>', 'y'): ('qcekbody', 'ε', 'X>'),
            ('qbody',' ','y'): ('qatrbody','ε','X'),
            ('qatrbody',' ','X') : ('qatrbody', 'ε' , 'ε'), #handler spasi di atribute
            ('qatrbody', '>', 'X'): ('qcekbody', 'ε', '>'),
            ('qcekbody', ' ', '>'): ('qcekbody', 'ε', 'ε'),

            ('qcekbody','/','>') : ('endbody','>','ε'),
            ('endbody', 'b', 'X'): ('endbody', 'X', 'ε'),
            ('endbody', 'o', 'y'): ('endbody', 'y', 'ε'),
            ('endbody', 'd', 'd'): ('endbody', 'd', 'ε'),
            ('endbody', 'y', 'o'): ('endbody', 'o', 'ε'),
            ('endbody', '>', 'b'): ('endbody', 'b', 'ε'),
            ('endbody', ' ', '<'): ('endbody', '<', 'ε'),
         
          

            #Q Attribute Body
            ('qatrbody','c','X') : ('qclassbody','ε', 'c'),
            ('qclassbody','l','c') : ('qclassbody','ε','l'),
            ('qclassbody','a','l') : ('qclassbody','ε','a'),
            ('qclassbody','s','a') : ('qclassbody','a','ε'),
            ('qclassbody','s','l') : ('qclassbody','l','ε'),
            ('qclassbody','=','c') : ('qclassbody','c','ε'),
            ('qclassbody','"','X') : ('qpetikbody','ε','"'),
            ('qpetikbody','"','"') : ('qatrbody' , '"','ε'),

            ('qatrbody','s','X') : ('qstylebody','ε', 's'),
            ('qstylebody','t','s') : ('qstylebody','ε','t'),
            ('qstylebody','y','t') : ('qstylebody','ε','y'),
            ('qstylebody','l','y') : ('qstylebody','y','ε'),
            ('qstylebody','e','t') : ('qstylebody','t','ε'),
            ('qstylebody','=','s') : ('qstylebody','s','ε'),
            ('qstylebody','"','X') : ('qpetikbody','ε','"'),
            ('qpetikbody','"','"') : ('qatrbody' , '"','ε'),

            ('qatrbody','i','X') : ('qidbody','ε', 'i'),
            ('qidbody','d','i') : ('qidbody','i','ε'),
            ('qidbody','=','X') : ('qidbody','ε','ε'),
            ('qidbody','"','X') : ('qpetikbody','ε','"'),
            ('qpetikbody','"','"') : ('qatrbody' , '"','ε'),

           

            #==============================HEAD============================
            ('qcek', '<', '>'): ('qcek', 'ε', '<'),
            ('qcek', 'h', '<'): ('qhead', 'ε', 'h'),
            ('qhead', 'e', 'h'): ('qhead', 'ε', 'e'),
            ('qhead', 'a', 'e'): ('qhead', 'ε', 'a'),
            ('qhead', 'd', 'a'): ('qhead', 'ε', 'd'),
            ('qhead', '>', 'd'): ('qcekhead', 'ε', 'X>'),
            ('qhead', ' ','d') : ('qatrhead' ,'ε','X'),
            ('qatrhead',' ','X') : ('qatrhead', 'ε' , 'ε'),
            ('qatrhead', '>', 'X'): ('qcekhead', 'ε', '>'),


            ('qcekhead', '/', '>'): ('endhead', '>', 'ε'),
            ('endhead', 'h', 'X'): ('endhead', 'X', 'ε'),
            ('endhead', 'e', 'd'): ('endhead', 'd', 'ε'),
            ('endhead', 'a', 'a'): ('endhead', 'a', 'ε'),
            ('endhead', 'd', 'e'): ('endhead', 'e', 'ε'),
            ('endhead', '>', 'h'): ('qcek', 'h', 'ε'),
            ('qcek', ' ', '<'): ('qcek', '<', 'ε'), #Spasial
            

             #Q Attribute Head
            ('qatrhead','c','X') : ('qclasshead','ε', 'c'),
            ('qclasshead','l','c') : ('qclasshead','ε','l'),
            ('qclasshead','a','l') : ('qclasshead','ε','a'),
            ('qclasshead','s','a') : ('qclasshead','a','ε'),
            ('qclasshead','s','l') : ('qclasshead','l','ε'),
            ('qclasshead','=','c') : ('qclasshead','c','ε'),
            ('qclasshead','"','X') : ('qpetikhead','ε','"'),
            ('qpetikhead','"','"') : ('qatrhead' , '"','ε'),

            ('qatrhead','s','X') : ('qstylehead','ε', 's'),
            ('qstylehead','t','s') : ('qstylehead','ε','t'),
            ('qstylehead','y','t') : ('qstylehead','ε','y'),
            ('qstylehead','l','y') : ('qstylehead','y','ε'),
            ('qstylehead','e','t') : ('qstylehead','t','ε'),
            ('qstylehead','=','s') : ('qstylehead','s','ε'),
            ('qstylehead','"','X') : ('qpetikhead','ε','"'),
            ('qpetikhead','"','"') : ('qatrhead' , '"','ε'),

            ('qatrhead','i','X') : ('qidhead','ε', 'i'),
            ('qidhead','d','i') : ('qidhead','i','ε'),
            ('qidhead','=','X') : ('qidhead','ε','ε'),
            ('qidhead','"','X') : ('qpetikhead','ε','"'),
            ('qpetikhead','"','"') : ('qatrhead' , '"','ε'),

            #==============================TITLE============================ (HEAD)
            ('qcekhead',' ','>') : ('qcekhead','ε','ε'), #handle spasi antar tag
            ('qcekhead', '<', '>'): ('qcekhead', 'ε', 'ε'),
            ('qcekhead', 't', '>'): ('qtitle', 'ε', '<t'),
            ('qtitle', 'i', 't'): ('qtitle', 'ε', 'i'),
            ('qtitle', 't', 'i'): ('qtitle', 'ε', 't'),
            ('qtitle', 'l', 't'): ('qtitle', 'ε', 'l'),
            ('qtitle', 'e', 'l'): ('qtitle', 'ε', 'e'),
            ('qtitle', ' ', 'e'): ('qatrtitle', 'ε', 'X'),
            ('qtitle', '>', 'e'): ('qtitle', 'ε', 'X>'),
            ('qatrtitle','>','X') : ('qtitle','ε','>'),
            ('qatrtitle',' ','X') : ('qatrtitle','ε', 'ε'), #Handler apabila ada spasi di atribute

            ('qtitle',' ','>') : ('qtitle','ε','ε'),
            ('qtitle','<','>') : ('endtitle','>','ε'),
            ('endtitle','/','X') : ('endtitle','X','ε'),
            ('endtitle','t','e') : ('endtitle','e','ε'),
            ('endtitle','i','l') : ('endtitle','l','ε'),
            ('endtitle','t','t') : ('endtitle','t','ε'),
            ('endtitle','l','i') : ('endtitle','i','ε'),
            ('endtitle','e','t') : ('endtitle','t','ε'),
            ('endtitle','>','<') : ('qcekhead','<','ε'),
            ('endtitle', ' ', '>'): ('endtitle', 'ε', 'ε'),

             #Q Attribute Title
            ('qatrtitle','c','X') : ('qclasstitle','ε', 'c'),
            ('qclasstitle','l','c') : ('qclasstitle','ε','l'),
            ('qclasstitle','a','l') : ('qclasstitle','ε','a'),
            ('qclasstitle','s','a') : ('qclasstitle','a','ε'),
            ('qclasstitle','s','l') : ('qclasstitle','l','ε'),
            ('qclasstitle','=','c') : ('qclasstitle','c','ε'),
            ('qclasstitle','"','X') : ('qpetiktitle','ε','"'),
            ('qpetiktitle','"','"') : ('qatrtitle' , '"','ε'),

            ('qatrtitle','s','X') : ('qstyletitle','ε', 's'),
            ('qstyletitle','t','s') : ('qstyletitle','ε','t'),
            ('qstyletitle','y','t') : ('qstyletitle','ε','y'),
            ('qstyletitle','l','y') : ('qstyletitle','y','ε'),
            ('qstyletitle','e','t') : ('qstyletitle','t','ε'),
            ('qstyletitle','=','s') : ('qstyletitle','s','ε'),
            ('qstyletitle','"','X') : ('qpetiktitle','ε','"'),
            ('qpetiktitle','"','"') : ('qatrtitle' , '"','ε'),

            
            ('qatrtitle','i','X') : ('qidtitle','ε', 'i'),
            ('qidtitle','d','i') : ('qidtitle','i','ε'),
            ('qidtitle','=','X') : ('qidtitle','ε','ε'),
            ('qidtitle','"','X') : ('qpetiktitle','ε','"'),
            ('qpetiktitle','"','"') : ('qatrtitle' , '"','ε'),


            #==============================LINK============================ (HEAD,BODY)
            ('qcekhead',' ','>') : ('qcekhead','ε','ε'), #handle spasi antar tag
            ('qcekhead', '<', '>'): ('qcekhead', 'ε', 'ε'),
            ('qcekhead', 'l', '>'): ('qlinkhead', 'ε', '<l'),
            ('qlinkhead', 'i', 'l'): ('qlinkhead', 'ε', 'i'),
            ('qlinkhead', 'n', 'i'): ('qlinkhead', 'ε', 'n'),
            ('qlinkhead', 'k', 'n'): ('qlinkhead', 'ε', 'k'),
            ('qlinkhead',' ', 'k'): ('qatrlinkhead','ε' ,'ε'),
            ('qatrlinkhead','r', 'k'): ('qlinkhead','k' ,'ε'),
            ('qlinkhead','e', 'n'): ('qlinkhead','n' ,'ε'),
            ('qlinkhead','l', 'i'): ('qlinkhead','i' ,'ε'),
            ('qlinkhead','=', 'l'): ('qlinkhead','l' ,'ε'),
            ('qlinkhead','"', '<'): ('qkutiplinkhead','ε' ,'"'),
            ('qkutiplinkhead','"', '"'): ('qlinkhead','"' ,'ε'),
            ('qlinkhead',' ','<') : ('qatrlinkhead','ε','ε'),
            ('qlinkhead','>','<') : ('qcekhead','<','ε'),
            ('qatrlinkhead','>','<') : ('qcekhead','<','ε'),
            ('qatrlinkhead',' ','<') : ('qatrlinkhead','ε', 'ε'), #Handler apabila ada spasi di atribute

            #Q Attribute Link
            ('qatrlinkhead','h','<') : ('qhreflinkhead','ε', 'h'),
            ('qhreflinkhead','r','h') : ('qhreflinkhead','ε','r'),
            ('qhreflinkhead','e','r') : ('qhreflinkhead','r','ε'),
            ('qhreflinkhead','f','h') : ('qhreflinkhead','h','ε'),
            ('qhreflinkhead','=','<') : ('qhreflinkhead','ε','ε'),
            ('qhreflinkhead','"','<') : ('qpetiklinkhead','ε','"'),
            ('qpetiklinkhead','"','"') : ('qatrlinkhead' , '"','ε'),
           
            
            
            ('qatrlinkhead','c','<') : ('qclasslinkhead','ε', 'c'),
            ('qclasslinkhead','l','c') : ('qclasslinkhead','ε','l'),
            ('qclasslinkhead','a','l') : ('qclasslinkhead','ε','a'),
            ('qclasslinkhead','s','a') : ('qclasslinkhead','a','ε'),
            ('qclasslinkhead','s','l') : ('qclasslinkhead','l','ε'),
            ('qclasslinkhead','=','c') : ('qclasslinkhead','c','ε'),
            ('qclasslinkhead','"','<') : ('qpetiklinkhead','ε','"'),
            ('qpetiklinkhead','"','"') : ('qatrlinkhead' , '"','ε'),

            ('qatrlinkhead','s','<') : ('qstylelinkhead','ε', 's'),
            ('qstylelinkhead','t','s') : ('qstylelinkhead','ε','t'),
            ('qstylelinkhead','y','t') : ('qstylelinkhead','ε','y'),
            ('qstylelinkhead','l','y') : ('qstylelinkhead','y','ε'),
            ('qstylelinkhead','e','t') : ('qstylelinkhead','t','ε'),
            ('qstylelinkhead','=','s') : ('qstylelinkhead','s','ε'),
            ('qstylelinkhead','"','<') : ('qpetiklinkhead','ε','"'),
            ('qpetiklinkhead','"','"') : ('qatrlinkhead' , '"','ε'),

            
            ('qatrlinkhead','i','<') : ('qidlinkhead','ε', 'i'),
            ('qidlinkhead','d','i') : ('qidlinkhead','i','ε'),
            ('qidlinkhead','=','<') : ('qidlinkhead','ε','ε'),
            ('qidlinkhead','"','<') : ('qpetiklinkhead','ε','"'),
            ('qpetiklinkhead','"','"') : ('qatrlinkhead' , '"','ε'),
             #==============================SCRIPT============================ (HEAD,BODY)
            ('qcekhead',' ','>') : ('qcekhead','ε','ε'), #handle spasi antar tag
            ('qcekhead', '<', '>'): ('qcekhead', 'ε', 'ε'),
            ('qcekhead', 's', '>'): ('qscript', 'ε', '<s'),
            ('qscript', 'c', 's'): ('qscript', 'ε', 'c'),
            ('qscript', 'r', 'c'): ('qscript', 'ε', 'r'),
            ('qscript', 'i', 'r'): ('qscript', 'ε', 'i'),
            ('qscript', 'p', 'i'): ('qscript', 'ε', 'p'),
            ('qscript', 't', 'p'): ('qscript', 'ε', 't'),
            ('qscript', ' ', 't'): ('qatrscript', 'ε', 'X'),
            ('qscript', '>', 't'): ('qscript', 'ε', 'X>'),
            ('qatrscript','>','X') : ('qscript','ε','>'),
            ('qatrscript',' ','X') : ('qatrscript','ε', 'ε'), #Handler apabila ada spasi di atribute

            ('qscript',' ','>') : ('qscript','ε','ε'),
            ('qscript','<','>') : ('endscript','>','ε'),
            ('endscript','/','X') : ('endscript','X','ε'),
            ('endscript','s','t') : ('endscript','t','ε'),
            ('endscript','c','p') : ('endscript','p','ε'),
            ('endscript','r','i') : ('endscript','i','ε'),
            ('endscript','i','r') : ('endscript','r','ε'),
            ('endscript','p','c') : ('endscript','c','ε'),
            ('endscript','t','s') : ('endscript','s','ε'),
            ('endscript','>','<') : ('qcekhead','<','ε'),
            ('endscript', ' ', '>'): ('endscript', 'ε', 'ε'),

             #Q Attribute script
            ('qatrscript','c','X') : ('qclassscript','ε', 'c'),
            ('qclassscript','l','c') : ('qclassscript','ε','l'),
            ('qclassscript','a','l') : ('qclassscript','ε','a'),
            ('qclassscript','s','a') : ('qclassscript','a','ε'),
            ('qclassscript','s','l') : ('qclassscript','l','ε'),
            ('qclassscript','=','c') : ('qclassscript','c','ε'),
            ('qclassscript','"','X') : ('qpetikscript','ε','"'),
            ('qpetikscript','"','"') : ('qatrscript' , '"','ε'),

            ('qatrscript','s','X') : ('qstylescript','ε', 's'),
            ('qstylescript','t','s') : ('qstylescript','ε','t'),
            ('qstylescript','y','t') : ('qstylescript','ε','y'),
            ('qstylescript','l','y') : ('qstylescript','y','ε'),
            ('qstylescript','e','t') : ('qstylescript','t','ε'),
            ('qstylescript','=','s') : ('qstylescript','s','ε'),
            ('qstylescript','"','X') : ('qpetikscript','ε','"'),
            ('qpetikscript','"','"') : ('qatrscript' , '"','ε'),

            
            ('qatrscript','i','X') : ('qidscript','ε', 'i'),
            ('qidscript','d','i') : ('qidscript','i','ε'),
            ('qidscript','=','X') : ('qidscript','ε','ε'),
            ('qidscript','"','X') : ('qpetikscript','ε','"'),
            ('qpetikscript','"','"') : ('qatrscript' , '"','ε'),

            ('qatrscript','s','X') : ('qsrcscript','ε', 's'),
            ('qsrcscript','r','s') : ('qsrcscript','ε','r'),
            ('qsrcscript','c','r') : ('qsrcscript','r','ε'),
            ('qsrcscript','=','s') : ('qsrcscript','s','ε'),
            ('qsrcscript','"','X') : ('qpetikscript','ε','"'),
            ('qpetikscript','"','"') : ('qatrscript' , '"','ε'),

         #==============================DIV==============================(BODY) patokand di body
           ('qcekbody', '<', '>'): ('qcekbody', 'ε', 'ε'),
           ('qcekbody', 'd', '>'): ('qdiv', 'ε', 'D<d'),
           ('qdiv', 'i', 'd'): ('qdiv', 'ε', 'i'),
           ('qdiv', 'v', 'i'): ('qdiv', 'ε', 'v'),
           ('qdiv', ' ', 'v'): ('qatrdiv', 'ε', 'X'),
           ('qdiv', '>', 'v'): ('qdiv', 'ε', 'X>'),
           ('qatrdiv','>','X') : ('qdiv','ε','>'),
           ('qatrdiv',' ','X') : ('qatrdiv','ε','ε'),
           ('qdiv', ' ', '>'): ('qdiv', 'ε', 'ε'),

           ('qdiv', '<', '>'): ('qdiv', 'ε', 'ε'),
           ('qdiv', 'd', '>'): ('qdiv', 'ε', '<d'),
           ('qdiv','<','D') : ('qcekbody','D','ε'),

           
           ('qdiv','<','>') : ('qdiv','ε','ε'),
           ('qdiv','/','>') : ('enddiv','>','ε'),
           ('enddiv','d','X') : ('enddiv','X','ε'),
           ('enddiv','i','v') : ('enddiv','v','ε'),
           ('enddiv','v','i') : ('enddiv','i','ε'),
           ('enddiv','>','d') : ('enddiv','d','ε'),
           ('enddiv',' ','<') : ('qdiv','<','ε'),
           ('enddiv','>','<') : ('enddiv','<','ε'),
           ('enddiv',' ','>') : ('qdiv','ε','ε'),


           #Q Attribute div
            ('qatrdiv','c','X') : ('qclassdiv','ε', 'c'),
            ('qclassdiv','l','c') : ('qclassdiv','ε','l'),
            ('qclassdiv','a','l') : ('qclassdiv','ε','a'),
            ('qclassdiv','s','a') : ('qclassdiv','a','ε'),
            ('qclassdiv','s','l') : ('qclassdiv','l','ε'),
            ('qclassdiv','=','c') : ('qclassdiv','c','ε'),
            ('qclassdiv','"','X') : ('qpetikdiv','ε','"'),
            ('qpetikdiv','"','"') : ('qatrdiv' , '"','ε'),

            ('qatrdiv','s','X') : ('qstylediv','ε', 's'),
            ('qstylediv','t','s') : ('qstylediv','ε','t'),
            ('qstylediv','y','t') : ('qstylediv','ε','y'),
            ('qstylediv','l','y') : ('qstylediv','y','ε'),
            ('qstylediv','e','t') : ('qstylediv','t','ε'),
            ('qstylediv','=','s') : ('qstylediv','s','ε'),
            ('qstylediv','"','X') : ('qpetikdiv','ε','"'),
            ('qpetikdiv','"','"') : ('qatrdiv' , '"','ε'),

            
            ('qatrdiv','i','X') : ('qiddiv','ε', 'i'),
            ('qiddiv','d','i') : ('qiddiv','i','ε'),
            ('qiddiv','=','X') : ('qiddiv','ε','ε'),
            ('qiddiv','"','X') : ('qpetikdiv','ε','"'),
            ('qpetikdiv','"','"') : ('qatrdiv' , '"','ε'),
             #==============================h1,h2,h3,h4,h5,h6==============================
            ('qcekbody', '<', '>'): ('qcekbody', 'ε', 'ε'),
            ('qcekbody', 'h', '>'): ('qh', 'ε', '<h'),
            ('qh', '1', 'h'): ('qh', 'ε', '1'),
            ('qh', '2', 'h'): ('qh', 'ε', '2'),
            ('qh', '3', 'h'): ('qh', 'ε', '3'),
            ('qh', '4', 'h'): ('qh', 'ε', '4'),
            ('qh', '5', 'h'): ('qh', 'ε', '5'),
            ('qh', '6', 'h'): ('qh', 'ε', '6'),
            ('qh',' ','1') : ('qatrh','ε','X'),
            ('qh',' ','2') : ('qatrh','ε','X'),
            ('qh',' ','3') : ('qatrh','ε','X'),
            ('qh',' ','4') : ('qatrh','ε','X'),
            ('qh',' ','5') : ('qatrh','ε','X'),
            ('qh',' ','6') : ('qatrh','ε','X'),
            ('qh' ,'>','1') : ('qh','ε','X>'),
            ('qh' ,'>','2') : ('qh','ε','X>'),
            ('qh' ,'>','3') : ('qh','ε','X>'),
            ('qh' ,'>','4') : ('qh','ε','X>'),
            ('qh' ,'>','5') : ('qh','ε','X>'),
            ('qh' ,'>','6') : ('qh','ε','X>'),
            ('qatrh','>','X') : ('qh','ε','>'),
            ('qatrh',' ','X') : ('qatrh','ε', 'ε'),

            ('qh',' ','>') : ('qh','ε','ε'),
            ('qh','<','>') : ('endh','>','ε'),
            ('endh','/','X') : ('endh','X','ε'),
            ('endh','h','1') : ('endh','1','ε'),
            ('endh','h','2') : ('endh','2','ε'),
            ('endh','h','3') : ('endh','3','ε'),
            ('endh','h','4') : ('endh','4','ε'),
            ('endh','h','5') : ('endh','5','ε'),
            ('endh','h','6') : ('endh','6','ε'),
            ('endh','1','h') : ('endh','h','ε'),
            ('endh','2','h') : ('endh','h','ε'),
            ('endh','3','h') : ('endh','h','ε'),
            ('endh','4','h') : ('endh','h','ε'),
            ('endh','5','h') : ('endh','h','ε'),
            ('endh','6','h') : ('endh','h','ε'),
            ('endh','>','<') : ('qcekbody','<','ε'),


            #Q Attribute h
            ('qatrh','c','X') : ('qclassh','ε', 'c'),
            ('qclassh','l','c') : ('qclassh','ε','l'),
            ('qclassh','a','l') : ('qclassh','ε','a'),
            ('qclassh','s','a') : ('qclassh','a','ε'),
            ('qclassh','s','l') : ('qclassh','l','ε'),
            ('qclassh','=','c') : ('qclassh','c','ε'),
            ('qclassh','"','X') : ('qpetikh','ε','"'),
            ('qpetikh','"','"') : ('qatrh' , '"','ε'),

            ('qatrh','s','X') : ('qstyleh','ε', 's'),
            ('qstyleh','t','s') : ('qstyleh','ε','t'),
            ('qstyleh','y','t') : ('qstyleh','ε','y'),
            ('qstyleh','l','y') : ('qstyleh','y','ε'),
            ('qstyleh','e','t') : ('qstyleh','t','ε'),
            ('qstyleh','=','s') : ('qstyleh','s','ε'),
            ('qstyleh','"','X') : ('qpetikh','ε','"'),
            ('qpetikh','"','"') : ('qatrh' , '"','ε'),

            
            ('qatrh','i','X') : ('qidh','ε', 'i'),
            ('qidh','d','i') : ('qidh','i','ε'),
            ('qidh','=','X') : ('qidh','ε','ε'),
            ('qidh','"','X') : ('qpetikh','ε','"'),
            ('qpetikh','"','"') : ('qatrh' , '"','ε'),
             #==============================p==============================
            ('qcekbody', '<', '>'): ('qcekbody', 'ε', 'ε'),
            ('qcekbody', 'p', '>'): ('qp', 'ε', '<p'),
            ('qp', ' ', 'p'): ('qatrp', 'ε', 'X'),
            ('qp', '>', 'p'): ('qp', 'ε', 'X>'),
            ('qatrp','>','X') :('qp', 'ε', '>'),
            ('qatrp',' ','X') : ('qatrp','ε','ε'),
            ('qp', ' ', '>'): ('qp', 'ε', 'ε'),
            
            ('qp','<','>') : ('endp','>','ε'),
            ('endp','/','X') : ('endp','X','ε'),
            ('endp','p','p') : ('endp','p','ε'),
            ('endp','>','<') : ('qcekbody','<','ε'),
          

            #Q Attribute p
            ('qatrp','c','X') : ('qclassp','ε', 'c'),
            ('qclassp','l','c') : ('qclassp','ε','l'),
            ('qclassp','a','l') : ('qclassp','ε','a'),
            ('qclassp','s','a') : ('qclassp','a','ε'),
            ('qclassp','s','l') : ('qclassp','l','ε'),
            ('qclassp','=','c') : ('qclassp','c','ε'),
            ('qclassp','"','X') : ('qpetikp','ε','"'),
            ('qpetikp','"','"') : ('qatrp' , '"','ε'),

            ('qatrp','s','X') : ('qstylep','ε', 's'),
            ('qstylep','t','s') : ('qstylep','ε','t'),
            ('qstylep','y','t') : ('qstylep','ε','y'),
            ('qstylep','l','y') : ('qstylep','y','ε'),
            ('qstylep','e','t') : ('qstylep','t','ε'),
            ('qstylep','=','s') : ('qstylep','s','ε'),
            ('qstylep','"','X') : ('qpetikp','ε','"'),
            ('qpetikp','"','"') : ('qatrp' , '"','ε'),

            
            ('qatrp','i','X') : ('qidp','ε', 'i'),
            ('qidp','d','i') : ('qidp','i','ε'),
            ('qidp','=','X') : ('qidp','ε','ε'),
            ('qidp','"','X') : ('qpetikp','ε','"'),
            ('qpetikp','"','"') : ('qatrp' , '"','ε'),
            #==============================br==============================V

            #==============================em==============================
            #==============================b==============================
            #==============================abbr==============================
            #==============================strong==============================
             #==============================small==============================
            
            
           
         
}


    # ('q1', '<', '>'): ('cek', '>', '>'), # gk berubah


    # #html to /html q1 -> end
    # ('cek','/','>') : ('end','>','ε'),
    # ('end','h','l') : ('end','l','ε'),
    # ('end','t','m') : ('end','m','ε'),
    # ('end','m','t') : ('end','t','ε'),
    # ('end','l','h') : ('end','h','ε'),
    # ('end','>','<') : ('end','<','ε'),


    # #html to head q1 -> q2
    # ('cek','h','>') : ('q2','ε','<h'),
    # ('q2','e','h') : ('q2','ε','e'),
    # ('q2','a','e') : ('q2','ε','a'),
    # ('q2','d','a') : ('q2','ε','d'),
    # ('q2','>','d') : ('q2','ε','>'),
  

    # #head q2 to end head -> balik ke q1(didalam html)
    # ('q2','<','>') : ('q2','>','>'),
    # ('q2','/','>') : ('endhead','>','ε'),
    # ('endhead','h','d') : ('endhead','d','ε'),
    # ('endhead','e','a') : ('endhead','a','ε'),
    # ('endhead','a','e') : ('endhead','e','ε'),
    # ('endhead','d','h') : ('endhead','h','ε'),
    # ('endhead','>','<') : ('q1','<','ε'),

    # #head to body
    # ('cek','h','>') : ('q2','ε','<h'),
    # ('q2','e','h') : ('q2','ε','e'),
    # ('q2','a','e') : ('q2','ε','a'),
    # ('q2','d','a') : ('q2','ε','d'),
    # ('q2','>','d') : ('q2','ε','>'),
  

    # #body to endbody
    # ('q2','<','>') : ('q2','>','>'),
    # ('q2','/','>') : ('endhead','>','ε'),
    # ('endhead','h','d') : ('endhead','d','ε'),
    # ('endhead','e','a') : ('endhead','a','ε'),
    # ('endhead','a','e') : ('endhead','e','ε'),
    # ('endhead','d','h') : ('endhead','h','ε'),
    # ('endhead','>','<') : ('q1','<','ε'),
    
    
    # ('q1', '', 'Z'): ('q2', 'ε', 'ε'),  # Penambahan transisi untuk membaca epsilon saat stack kosong
start_state = 'q0'
initial_stack_symbol = 'Z'

pda = PDA(states, input_alphabet, stack_alphabet, transition, start_state, initial_stack_symbol)

# Mendapatkan path dari direktori saat ini
current_directory = os.getcwd()
# Path dari direktori parent untuk file atau direktori tertentu
file_path = os.path.join(current_directory,'src', 'example.html')

with open(file_path, 'r') as file:
    # Membaca seluruh konten file
    html_content = file.read()

# Sekarang, variabel html_content berisi seluruh string dari file HTML
splittedcontent = html_content.split()
result_string = " ".join(splittedcontent)

print(result_string)

result = pda.process_input(result_string)

if result:
    print(f"Input '{result_string}' is accepted.")
else:
    print(f"Input '{result_string}' is not accepted.")
