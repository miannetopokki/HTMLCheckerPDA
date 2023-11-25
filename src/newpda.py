import os
import ast

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
            transition_key = (self.current_state, symbol, self.stack[-1])
            transition_tuple = self.transition.get(transition_key)

            
            if transition_tuple is not None:
                # print(f"Transition tuple found: {transition_tuple}")
                next_state, pop_symbol, push_symbols = transition_tuple

           
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
                print(f"SAAT iNI : ({self.current_state}, {symbol}, {self.stack[-1]}).")
                print(self.stack)
            elif (self.current_state != 'qpetikbody' and self.current_state != 'qpetikhead'and self.current_state != 'qpetikhtml'
                    and self.current_state != 'qpetiktitle' and self.current_state != 'qpetiklinkhead' and self.current_state != 'qkutiplinkhead'
                    and self.current_state != 'qdiv' and self.current_state != 'qpetikhr' and self.current_state != 'qpetika'
                    and self.current_state != "qpetikdiv" and self.current_state != "qtitle"  and self.current_state != "qhcek" and self.current_state != "qpcek"):   #Handler ignorance
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
          'qdiv','qatrdiv','enddiv','qpetikdiv','qclassdiv','qiddiv','qstylediv','qcekdiv',
          'qh','endh','qatrh','qclassh','qidh','qpetikh','qstyleh','qhcek',
          'qp','qatrp','endp','qclassp','qidp','qpetikp','qstylep','qcekp',
          'qhr','qatrhr','qclasshr','qidhr','qpetikhr','qstylehr', 'q=hr',
          'qa','enda','qatra','qclassa','qida','qpetika','qstylea', 'q=a', 'qhrefa',
          'qimg','qatrimg','qclassimg','qidimg','qpetikimg','qstyleimg', 'qatrsrcimg', 'qsrcimg', 'qaltimg', 'q=img',
          'qclasssrcimg','qidsrcimg','qpetiksrcimg','qstylesrcimg','qaltsrcimg', 'q=srcimg',
          'qbutton','endbutton','qatrbutton','qclassbutton','qidbutton','qpetikbutton','qstylebutton', 'q=button', 'qsubmitbutton', 'qresetbutton', 'q=resetbutton','qbuttonbutton', 'qpetiktypebutton', 'qtypebutton',
          'qform','endform','qatrform','qclassform','qidform','qpetikform','qstyleform', 'q=form', 'qactionform', 'qgetform', 'q=getform','qformform', 'qpetikmethod', 'qmethodform',
          'qinput','endinput','qatrinput','qclassinput','qidinput','qpetikinput','qstyleinput', 'q=input', 'qnumberinput', 'qcheckboxinput', 'q=emailinput','qemailinput','qpasswordinput', 'qpetiktypeinput', 'qtypeinput',
          'qbr',
          'qem','qatrem','endem','qclassem','qstyleem','qidem','qcekem','qepetikem',
          'qsmall','qatrsmall','qclasssmall','qidsmall','qstylesmall','endsmall','qceksmall','qepetiksmall',
          'qstrong','qatrstrong','qclassstrong','qidstrong','qstylestrong','endstrong','qcekstrong','qepetikstrong',
          'qtable', 'qcektable','endtable', 'qatrtable','qclasstable','qidtable','qpetiktable','qstyletable', 'qatrsrctable', 'qsrctable', 'qalttable', 'q=table',
          'qtr', 'endtr', 'qatrtr','qclasstr','qidtr','qpetiktr','qstyletr', 'qatrsrctr', 'qsrctr', 'qalttr', 'q=tr', 'endt',
          'qtd', 'endtd', 'qatrtd','qclasstd','qidtd','qpetiktd','qstyletd', 'qatrsrctd', 'qsrctd', 'qalttd', 'q=td',
          'qth', 'endth', 'qatrth','qclassth','qidth','qpetikth','qstyleth', 'qatrsrcth', 'qsrcth', 'qaltth', 'q=th',
          'qabbr','endabbr','qatrabbr','qclassabr','qidabbr','qpetikabbr','qstyleabbr','qcekabbr'} 
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

       
           ('qcekdiv', 'd', '>'): ('qdiv', 'ε', '<d'),
           ('qdiv','<','D') : ('qcekbody','D','ε'), #POP D agar balik ke body

           ('qcekdiv','p','>') : ('qp','ε','Dp'), #Ada <p> di dalam div
           ('qcekdiv','h','>') : ('qh','ε','Dh'), #ada <h> di dlaam div

           
           ('qdiv','<','>') : ('qcekdiv','ε','ε'),
           ('qcekdiv','/','>') : ('enddiv','>','ε'),
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
            ('qh', 'r', 'h'): ('qhr', 'h', 'ε'),
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
            ('qatrh','>','X') : ('qhcek','ε','>'),
            ('qatrh',' ','X') : ('qatrh','ε', 'ε'),

       
            ('qh',' ','>') : ('qh','ε','ε'),
            ('qh','<','>') : ('qhcek','ε','ε'),

            ('qhcek','/','>') : ('endh','>','ε'),
            ('endh','h','X') : ('endh','X','ε'),
            ('endh','1','1') : ('endh','1','ε'),
            ('endh','2','2') : ('endh','2','ε'),
            ('endh','3','3') : ('endh','3','ε'),
            ('endh','4','4') : ('endh','4','ε'),
            ('endh','5','5') : ('endh','5','ε'),
            ('endh','6','6') : ('endh','6','ε'),
            ('endh','>','h') : ('endh','h','ε'),
            ('endh',' ','<') : ('qcekbody','<','ε'),

            ('qhcek','p','>') : ('qp','ε','Hp'), #H symbol di <h_>

            ('endh',' ','D') : ('qdiv','D','ε'), #H di dalam nest div
            




           


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
            ('qcekbody', 'p', '>'): ('qp', 'ε', '<p'), #p sebagai parent nest
            ('qp', ' ', 'p'): ('qatrp', 'ε', 'X'),
            ('qp', '>', 'p'): ('qp', 'ε', 'X>'),
            ('qatrp','>','X') :('qp', 'ε', '>'),
            ('qatrp',' ','X') : ('qatrp','ε','ε'),
            ('qp', ' ', '>'): ('qp', 'ε', 'ε'),
            
            
            ('qcekp','e','>') : ('qem','ε','Pe'),
            ('qcekp','s','>') : ('qcekbody','ε','Ps'),
            ('qcekp','a','>') : ('qa','ε','Pa'), #cek a atau abbr

            ('qp','<','>') : ('qcekp','ε','ε'),
            ('qcekp','<','>') : ('qcekp','ε','ε'),
            ('qcekp','/','>') : ('endp','>','ε'),
            ('endp','p','X') : ('endp','X','ε'),
            ('endp','>','p') : ('endp','p','ε'),
            ('endp',' ','<') : ('qcekbody','<','ε'),
            
          
            #Handler 'p' di nesting lain
            ('endp',' ','H') : ('qh','H','ε'), # di dalam nest h

            ('endp',' ','P') : ('qcekbody','P','ε'),

            ('endp',' ','D') : ('qdiv','D','ε'), # didalam div

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
            #==============================br==============================
            ('qbutton','r','b') : ('qbr','b','ε'),
            ('qbr','>','<'):('qcekbody','<','ε'),

            #==============================em==============================
            ('qcekbody','<','>') : ('qcekbody','ε','ε'),
            ('qcekbody','e','>') : ('qem','ε','<e'),
            ('qem','m','e') : ('qem','ε','m'),
            ('qem','>','m') : ('qcekem','ε','X>'),
            ('qem',' ','m') : ('qatrem','ε','X'),
            ('qatrem','>','X') : ('qcekem','ε','>'),

            

            ('qcekem',' ','>') : ('qcekem','ε','ε'),
            ('qcekem','<','>') : ('qcekem','ε','ε'),
            ('qcekem','/','>') : ('endem','>','ε'),
            ('endem','e','X') : ('endem','X','ε'),
            ('endem','m','m') : ('endem','m','ε'),
            ('endem','>','e') : ('endem','e','ε'),
            ('endem',' ','<') : ('qcekbody','<','ε'), #brarti hanya di dalam nest body

            ('endem',' ','P') : ('qcekp','P','ε'), #didalam nest 'p'
            ('endem',' ','S') : ('qceksmall','S','ε'), #didalam nest 'small'
            ('endem',' ','T') : ('qcekstrong','T','ε'), #didalam nest 'strong' 

            

            


            #Attribute em
            ('qatrem','c','X') : ('qclassem','ε', 'c'),
            ('qclassem','l','c') : ('qclassem','ε','l'),
            ('qclassem','a','l') : ('qclassem','ε','a'),
            ('qclassem','s','a') : ('qclassem','a','ε'),
            ('qclassem','s','l') : ('qclassem','l','ε'),
            ('qclassem','=','c') : ('qclassem','c','ε'),
            ('qclassem','"','X') : ('qepetikem','ε','"'),
            ('qepetikem','"','"') : ('qatrem' , '"','ε'),

            ('qatrem','s','X') : ('qstyleem','ε', 's'),
            ('qstyleem','t','s') : ('qstyleem','ε','t'),
            ('qstyleem','y','t') : ('qstyleem','ε','y'),
            ('qstyleem','l','y') : ('qstyleem','y','ε'),
            ('qstyleem','e','t') : ('qstyleem','t','ε'),
            ('qstyleem','=','s') : ('qstyleem','s','ε'),
            ('qstyleem','"','X') : ('qepetikem','ε','"'),
            ('qepetikem','"','"') : ('qatrem' , '"','ε'),

            
            ('qatrem','i','X') : ('qidem','ε', 'i'),
            ('qidem','d','i') : ('qidem','i','ε'),
            ('qidem','=','X') : ('qidem','ε','ε'),
            ('qidem','"','X') : ('qepetikem','ε','"'),
            ('qepetikem','"','"') : ('qatrem' , '"','ε'),
            

            

            #==============================b==============================
            #==============================abbr==============================
            ('qcekbody','<','>') : ('qcekbody','ε','ε'),
            ('qcekbody', 'a', '>'): ('qa', 'ε', '<a'),
            ('qa','b','a') : ('qabbr' ,'ε', 'b'), #handling dari <a> ke <abbr> 
            ('qabbr','b','b') : ('qabbr','ε','b'),
            ('qabbr','r','b') : ('qabbr','ε','r'),
            ('qabbr','>','r') : ('qabbr','ε','X>'),
            ('qabbr',' ','l') : ('qatrabbr','ε','X'),
            ('qatrabbr','>','X') : ('qabbr','ε','>'),
            ('qabbr',' ','>') : ('qabbr','ε','ε'),



            ('qabbr','<','>') : ('qcekabbr','ε','ε'),
            ('qcekabbr','<','>') : ('qcekabbr','ε','ε'),
            ('qcekabbr','/','>') : ('endabbr','>','ε'),
            ('endabbr','a','X') : ('endabbr','X','ε'),
            ('endabbr','b','r') : ('endabbr','r','ε'),
            ('endabbr','b','b') : ('endabbr','b','ε'),
            ('endabbr','r','b') : ('endabbr','b','ε'),
            ('endabbr','>','a') : ('endabbr','a','ε'),
            ('endabbr','>','s') : ('endabbr','s','ε'),

            ('endabbr',' ','<') : ('qcekbody','<','ε'), #didalam body
            ('endabbr',' ','P') : ('qp','P','ε'), #didalam p




            #Attribute abbr
            ('qatrabbr','c','X') : ('qclassabbr','ε', 'c'),
            ('qclassabbr','l','c') : ('qclassabbr','ε','l'),
            ('qclassabbr','a','l') : ('qclassabbr','ε','a'),
            ('qclassabbr','s','a') : ('qclassabbr','a','ε'),
            ('qclassabbr','s','l') : ('qclassabbr','l','ε'),
            ('qclassabbr','=','c') : ('qclassabbr','c','ε'),
            ('qclassabbr','"','X') : ('qepetikabbr','ε','"'),
            ('qepetikabbr','"','"') : ('qatrabbr' , '"','ε'),

            ('qatrabbr','s','X') : ('qstyleabbr','ε', 's'),
            ('qstyleabbr','t','s') : ('qstyleabbr','ε','t'),
            ('qstyleabbr','y','t') : ('qstyleabbr','ε','y'),
            ('qstyleabbr','l','y') : ('qstyleabbr','y','ε'),
            ('qstyleabbr','e','t') : ('qstyleabbr','t','ε'),
            ('qstyleabbr','=','s') : ('qstyleabbr','s','ε'),
            ('qstyleabbr','"','X') : ('qepetikabbr','ε','"'),
            ('qepetikabbr','"','"') : ('qatrabbr' , '"','ε'),

            
            ('qatrabbr','i','X') : ('qidabbr','ε', 'i'),
            ('qidabbr','d','i') : ('qidabbr','i','ε'),
            ('qidabbr','=','X') : ('qidabbr','ε','ε'),
            ('qidabbr','"','X') : ('qepetikabbr','ε','"'),
            ('qepetikabbr','"','"') : ('qatrabbr' , '"','ε'),
            #==============================strong==============================
            ('qcekbody','<','>') : ('qcekbody','ε','ε'),
            ('qcekbody','s','>') : ('qcekbody','ε','<s'),
            ('qcekbody','t','s') : ('qstrong','ε','t'),
            ('qstrong','r','t') : ('qstrong','ε','r'),
            ('qstrong','o','r') : ('qstrong','ε','o'),
            ('qstrong','n','o') : ('qstrong','ε','n'),
            ('qstrong','g','n') : ('qstrong','ε','g'),
            ('qstrong','>','g') : ('qstrong','ε','X>'),
            ('qstrong',' ','l') : ('qatrstrong','ε','X'),
            ('qatrstrong','>','X') : ('qstrong','ε','>'),
            ('qstrong',' ','>') : ('qstrong','ε','ε'),


            ('qcekstrong','e','>') : ('qem','ε','Te'),

            ('qstrong','<','>') : ('qcekstrong','ε','ε'),
            ('qcekstrong','<','>') : ('qcekstrong','ε','ε'),
            ('qcekstrong','/','>') : ('endstrong','>','ε'),
            ('endstrong','s','X') : ('endstrong','X','ε'),
            ('endstrong','t','g') : ('endstrong','g','ε'),
            ('endstrong','r','n') : ('endstrong','n','ε'),
            ('endstrong','o','o') : ('endstrong','o','ε'),
            ('endstrong','n','r') : ('endstrong','r','ε'),
            ('endstrong','g','t') : ('endstrong','t','ε'),
            ('endstrong','>','s') : ('endstrong','s','ε'),

            ('endstrong',' ','P') : ('qcekp','P','ε'), #didalam nest 'p'

            ('endstrong','>','p') : ('endstrong','p','ε'),
            ('endstrong',' ','<') : ('qcekbody','<','ε'),


            #Attribute strong
            ('qatrstrong','c','X') : ('qclassstrong','ε', 'c'),
            ('qclassstrong','l','c') : ('qclassstrong','ε','l'),
            ('qclassstrong','a','l') : ('qclassstrong','ε','a'),
            ('qclassstrong','s','a') : ('qclassstrong','a','ε'),
            ('qclassstrong','s','l') : ('qclassstrong','l','ε'),
            ('qclassstrong','=','c') : ('qclassstrong','c','ε'),
            ('qclassstrong','"','X') : ('qepetikstrong','ε','"'),
            ('qepetikstrong','"','"') : ('qatrstrong' , '"','ε'),

            ('qatrstrong','s','X') : ('qstylestrong','ε', 's'),
            ('qstylestrong','t','s') : ('qstylestrong','ε','t'),
            ('qstylestrong','y','t') : ('qstylestrong','ε','y'),
            ('qstylestrong','l','y') : ('qstylestrong','y','ε'),
            ('qstylestrong','e','t') : ('qstylestrong','t','ε'),
            ('qstylestrong','=','s') : ('qstylestrong','s','ε'),
            ('qstylestrong','"','X') : ('qepetikstrong','ε','"'),
            ('qepetikstrong','"','"') : ('qatrstrong' , '"','ε'),

            
            ('qatrstrong','i','X') : ('qidstrong','ε', 'i'),
            ('qidstrong','d','i') : ('qidstrong','i','ε'),
            ('qidstrong','=','X') : ('qidstrong','ε','ε'),
            ('qidstrong','"','X') : ('qepetikstrong','ε','"'),
            ('qepetikstrong','"','"') : ('qatrstrong' , '"','ε'),
            #==============================small==============================
            ('qcekbody','<','>') : ('qcekbody','ε','ε'),
            ('qcekbody','s','>') : ('qcekbody','ε','<s'),
            ('qcekbody','m','s') : ('qsmall','ε','m'),
            ('qsmall','a','m') : ('qsmall','ε','a'),
            ('qsmall','l','a') : ('qsmall','ε','l'),
            ('qsmall','l','l') : ('qsmall','ε','l'),
            ('qsmall','>','l') : ('qsmall','ε','X>'),
            ('qsmall',' ','l') : ('qatrsmall','ε','X'),
            ('qatrsmall','>','X') : ('qsmall','ε','>'),
            ('qsmall',' ','>') : ('qsmall','ε','ε'),

            ('endsmall',' ','P') : ('qcekp','P','ε'), #didalam nest 'p'


            ('qceksmall','e','>') : ('qem','ε','Se'),

            ('qsmall','<','>') : ('qceksmall','ε','ε'),
            ('qceksmall','<','>') : ('qceksmall','ε','ε'),
            ('qceksmall','/','>') : ('endsmall','>','ε'),
            ('endsmall','s','X') : ('endsmall','X','ε'),
            ('endsmall','m','l') : ('endsmall','l','ε'),
            ('endsmall','a','l') : ('endsmall','l','ε'),
            ('endsmall','l','a') : ('endsmall','a','ε'),
            ('endsmall','l','m') : ('endsmall','m','ε'),
            ('endsmall','>','s') : ('endsmall','s','ε'),

            ('endsmall','>','p') : ('endsmall','p','ε'),
            ('endsmall',' ','<') : ('qcekbody','<','ε'),


            #Attribute small
            ('qatrsmall','c','X') : ('qclasssmall','ε', 'c'),
            ('qclasssmall','l','c') : ('qclasssmall','ε','l'),
            ('qclasssmall','a','l') : ('qclasssmall','ε','a'),
            ('qclasssmall','s','a') : ('qclasssmall','a','ε'),
            ('qclasssmall','s','l') : ('qclasssmall','l','ε'),
            ('qclasssmall','=','c') : ('qclasssmall','c','ε'),
            ('qclasssmall','"','X') : ('qepetiksmall','ε','"'),
            ('qepetiksmall','"','"') : ('qatrsmall' , '"','ε'),

            ('qatrsmall','s','X') : ('qstylesmall','ε', 's'),
            ('qstylesmall','t','s') : ('qstylesmall','ε','t'),
            ('qstylesmall','y','t') : ('qstylesmall','ε','y'),
            ('qstylesmall','l','y') : ('qstylesmall','y','ε'),
            ('qstylesmall','e','t') : ('qstylesmall','t','ε'),
            ('qstylesmall','=','s') : ('qstylesmall','s','ε'),
            ('qstylesmall','"','X') : ('qepetiksmall','ε','"'),
            ('qepetiksmall','"','"') : ('qatrsmall' , '"','ε'),

            
            ('qatrsmall','i','X') : ('qidsmall','ε', 'i'),
            ('qidsmall','d','i') : ('qidsmall','i','ε'),
            ('qidsmall','=','X') : ('qidsmall','ε','ε'),
            ('qidsmall','"','X') : ('qepetiksmall','ε','"'),
            ('qepetiksmall','"','"') : ('qatrsmall' , '"','ε'),


            #==============================hr===============================
            ('qh', 'r', 'h'): ('qhr', 'h', 'ε'),
            ('qhr', ' ', '<'): ('qatrhr', '<', 'X'),
            ('qhr', '>', '<'): ('qcekbody', '<', 'ε'),
            ('qatrhr','>','X') :('qcekbody', 'X', 'ε'),
            ('qatrhr',' ','X') : ('qatrhr','ε','ε'),
            ('qhr', ' ', 'X'): ('qhr', 'ε', 'ε'),


            #atribut hr
            ('qatrhr','c','X') : ('qclasshr','ε', 'c'),
            ('qclasshr','l','c') : ('qclasshr','ε','l'),
            ('qclasshr','a','l') : ('qclasshr','ε','a'),
            ('qclasshr','s','a') : ('qclasshr','a','ε'),
            ('qclasshr','s','l') : ('qclasshr','l','ε'),
            ('qclasshr','=','c') : ('qclasshr','c','ε'),
            ('qclasshr','"','X') : ('qpetikhr','ε','"'),
            ('qpetikhr','"','"') : ('qatrhr' , '"','ε'),

            ('qatrhr','s','X') : ('qstylehr','ε', 's'),
            ('qstylehr','t','s') : ('qstylehr','ε','t'),
            ('qstylehr','y','t') : ('qstylehr','ε','y'),
            ('qstylehr','l','y') : ('qstylehr','y','ε'),
            ('qstylehr','e','t') : ('qstylehr','t','ε'),
            ('qstylehr','=','s') : ('qstylehr','s','ε'),
            ('qstylehr','"','X') : ('qpetikhr','ε','"'),
            ('qpetikhr','"','"') : ('qatrhr' , '"','ε'),

            
            ('qatrhr','i','X') : ('qidhr','ε', 'i'),
            ('qidhr','d','i') : ('qidhr','i','ε'),
            ('qidhr','=','X') : ('q=hr','ε','ε'),
            ('q=hr','"','X') : ('qpetikhr','ε','"'),
            ('qpetikhr','"','"') : ('qatrhr' , '"','ε'),

            #==============================endhr===============================


            #==============================a===============================
            
            ('qa', ' ', 'a'): ('qatra', 'ε', 'X'),
            ('qa', '>', 'a'): ('qa', 'ε', 'X>'),
            ('qatra','>','X') :('qa', 'ε', '>'),
            ('qatra',' ','X') : ('qatra','ε','ε'),
            ('qa', ' ', 'X'): ('qa', 'ε', 'ε'),

            ('qa',' ','>') : ('qa','ε','ε'),
            ('qa','<','>') : ('enda','>','ε'),
            ('enda','/','X') : ('enda','X','ε'),
            ('enda','a','a') : ('enda','a','ε'),
            ('enda','>','<') : ('qcekbody','<','ε'),

            ('enda','>','P') : ('qp','P','ε'), # didalam nest <p>

            #atribut a
            ('qatra','h','X') : ('qhrefa','ε', 'h'),
            ('qhrefa','r','h') : ('qhrefa','ε','r'),
            ('qhrefa','e','r') : ('qhrefa','r','ε'),
            ('qhrefa','f','h') : ('qhrefa','h','ε'),
            ('qhrefa','=','X') : ('q=a','ε','ε'),
            ('q=a','"','X') : ('qpetika','ε','"'),
            ('qpetika','"','"') : ('qatra' , '"','ε'),
            
            ('qatra','c','X') : ('qclassa','ε', 'c'),
            ('qclassa','l','c') : ('qclassa','ε','l'),
            ('qclassa','a','l') : ('qclassa','ε','a'),
            ('qclassa','s','a') : ('qclassa','a','ε'),
            ('qclassa','s','l') : ('qclassa','l','ε'),
            ('qclassa','=','c') : ('qclassa','c','ε'),
            ('qclassa','"','X') : ('qpetika','ε','"'),
            ('qpetika','"','"') : ('qatra' , '"','ε'),

            ('qatra','s','X') : ('qstylea','ε', 's'),
            ('qstylea','t','s') : ('qstylea','ε','t'),
            ('qstylea','y','t') : ('qstylea','ε','y'),
            ('qstylea','l','y') : ('qstylea','y','ε'),
            ('qstylea','e','t') : ('qstylea','t','ε'),
            ('qstylea','=','s') : ('qstylea','s','ε'),
            ('qstylea','"','X') : ('qpetika','ε','"'),
            ('qpetika','"','"') : ('qatra' , '"','ε'),

            ('qatra','i','X') : ('qida','ε', 'i'),
            ('qida','d','i') : ('qida','i','ε'),
            ('qida','=','X') : ('q=a','ε','ε'),
            ('q=a','"','X') : ('qpetika','ε','"'),
            ('qpetika','"','"') : ('qatra' , '"','ε'),
            #==============================enda===============================

            #==============================img==================================
            ('qcekbody', 'i', '>'): ('qimg', 'ε', '<i'),
            ('qimg', 'm', 'i'): ('qimg', 'i', 'ε'),
            ('qimg', 'g', '<'): ('qimg', '<', 'ε'),
            ('qimg', ' ', '>'): ('qatrimg', '', 'X'),
            ('qatrsrcimg','>','X') :('qcekbody', 'X', 'ε'),
            ('qatrimg',' ','X') : ('qatrimg','ε','ε'),
            ('qatrsrcimg',' ','X') : ('qatrsrcimg','ε','ε'),
            ('qimg', ' ', 'X'): ('qimg', 'ε', 'ε'),


            #atribut img
            ('qatrimg','c','X') : ('qclassimg','ε', 'c'),
            ('qclassimg','l','c') : ('qclassimg','ε','l'),
            ('qclassimg','a','l') : ('qclassimg','ε','a'),
            ('qclassimg','s','a') : ('qclassimg','a','ε'),
            ('qclassimg','s','l') : ('qclassimg','l','ε'),
            ('qclassimg','=','c') : ('qclassimg','c','ε'),
            ('qclassimg','"','X') : ('qpetikimg','ε','"'),
            ('qpetikimg','"','"') : ('qatrimg' , '"','ε'),

            ('qatrimg','s','X') : ('qstyleimg','ε', 's'),
            ('qstyleimg','t','s') : ('qstyleimg','ε','t'),
            ('qstyleimg','y','t') : ('qstyleimg','ε','y'),
            ('qstyleimg','l','y') : ('qstyleimg','y','ε'),
            ('qstyleimg','e','t') : ('qstyleimg','t','ε'),
            ('qstyleimg','=','s') : ('qstyleimg','s','ε'),
            ('qstyleimg','"','X') : ('qpetikimg','ε','"'),
            ('qpetikimg','"','"') : ('qatrimg' , '"','ε'),

            ('qatrimg','i','X') : ('qidimg','ε', 'i'),
            ('qidimg','d','i') : ('qidimg','i','ε'),
            ('qidimg','=','X') : ('q=img','ε','ε'),
            ('q=img','"','X') : ('qpetikimg','ε','"'),
            ('qpetikimg','"','"') : ('qatrimg' , '"','ε'),
            
            ('qatrimg','a','X') : ('qaltimg','ε', 'a'),
            ('qaltimg','l','a') : ('qaltimg','ε','l'),
            ('qaltimg','t','l') : ('qaltimg','l','ε'),
            ('qaltimg','=','a') : ('qaltimg','a','ε'),
            ('qaltimg','"','X') : ('qpetikimg','ε','"'),
            ('qpetikimg','"','"') : ('qatrimg' , '"','ε'),

            ('qatrimg','s','X') : ('qsrcimg','ε', 's'),
            ('qsrcimg','r','s') : ('qsrcimg','ε','r'),
            ('qsrcimg','c','r') : ('qsrcimg','r','ε'),
            ('qsrcimg','=','s') : ('qsrcimg','s','ε'),
            ('qsrcimg','"','X') : ('qpetiksrcimg','ε','"'),
            ('qpetiksrcimg','"','"') : ('qatrsrcimg' , '"','ε'),

            ('qatrsrcimg','c','X') : ('qclasssrcimg','ε', 'c'),
            ('qclasssrcimg','l','c') : ('qclasssrcimg','ε','l'),
            ('qclasssrcimg','a','l') : ('qclasssrcimg','ε','a'),
            ('qclasssrcimg','s','a') : ('qclasssrcimg','a','ε'),
            ('qclasssrcimg','s','l') : ('qclasssrcimg','l','ε'),
            ('qclasssrcimg','=','c') : ('qclasssrcimg','c','ε'),
            ('qclasssrcimg','"','X') : ('qpetiksrcimg','ε','"'),
            ('qpetiksrcimg','"','"') : ('qatrsrcimg' , '"','ε'),

            ('qatrsrcimg','s','X') : ('qstylesrcimg','ε', 's'),
            ('qstylesrcimg','t','s') : ('qstylesrcimg','ε','t'),
            ('qstylesrcimg','y','t') : ('qstylesrcimg','ε','y'),
            ('qstylesrcimg','l','y') : ('qstylesrcimg','y','ε'),
            ('qstylesrcimg','e','t') : ('qstylesrcimg','t','ε'),
            ('qstylesrcimg','=','s') : ('qstylesrcimg','s','ε'),
            ('qstylesrcimg','"','X') : ('qpetiksrcimg','ε','"'),
            ('qpetiksrcimg','"','"') : ('qatrsrcimg' , '"','ε'),

            ('qatrsrcimg','i','X') : ('qidsrcimg','ε', 'i'),
            ('qidsrcimg','d','i') : ('qidsrcimg','i','ε'),
            ('qidsrcimg','=','X') : ('q=srcimg','ε','ε'),
            ('q=srcimg','"','X') : ('qpetiksrcimg','ε','"'),
            ('qpetiksrcimg','"','"') : ('qatrsrcimg' , '"','ε'),
            
            ('qatrsrcimg','a','X') : ('qaltsrcimg','ε', 'a'),
            ('qaltsrcimg','l','a') : ('qaltsrcimg','ε','l'),
            ('qaltsrcimg','t','l') : ('qaltsrcimg','l','ε'),
            ('qaltsrcimg','=','a') : ('qaltsrcimg','a','ε'),
            ('qaltsrcimg','"','X') : ('qpetiksrcimg','ε','"'),
            ('qpetiksrcimg','"','"') : ('qatrsrcimg' , '"','ε'),
            #==============================endimg===============================
            

            #==============================button===============================
            ('qcekbody', 'b', '>'): ('qbutton', 'ε', '<b'),
            ('qbutton', 'u', 'b'): ('qbutton', 'ε', 'u'),
            ('qbutton', 't', 'u'): ('qbutton', 'ε', 't'),
            ('qbutton', 't', 't'): ('qbutton', 'ε', 't'),
            ('qbutton', 'o', 't'): ('qbutton', 'ε', 'o'),
            ('qbutton', 'n', 'o'): ('qbutton', 'ε', 'n'),
            ('qbutton', ' ', 'n'): ('qatrbutton', 'ε', 'X'),
            ('qbutton', '>', 'n'): ('qbutton', 'ε', 'X>'),
            ('qatrbutton','>','X') :('qbutton', 'ε', '>'),
            ('qatrbutton',' ','X') : ('qatrbutton','ε','ε'),
            ('qbutton', ' ', 'X'): ('qbutton', 'ε', 'ε'),

            ('qbutton',' ','>') : ('qbutton','ε','ε'),
            ('qbutton','<','>') : ('endbutton','>','ε'),
            ('endbutton','/','X') : ('endbutton','X','ε'),
            ('endbutton','b','n') : ('endbutton','n','ε'),
            ('endbutton','u','o') : ('endbutton','o','ε'),
            ('endbutton','t','t') : ('endbutton','t','ε'),
            ('endbutton','t','t') : ('endbutton','t','ε'),
            ('endbutton','o','u') : ('endbutton','u','ε'),
            ('endbutton','n','b') : ('endbutton','b','ε'),
            ('endbutton','>','<') : ('qcekbody','<','ε'),

            #atribut button
            ('qatrbutton','c','X') : ('qclassbutton','ε', 'c'),
            ('qclassbutton','l','c') : ('qclassbutton','ε','l'),
            ('qclassbutton','a','l') : ('qclassbutton','ε','a'),
            ('qclassbutton','s','a') : ('qclassbutton','a','ε'),
            ('qclassbutton','s','l') : ('qclassbutton','l','ε'),
            ('qclassbutton','=','c') : ('qclassbutton','c','ε'),
            ('qclassbutton','"','X') : ('qpetikbutton','ε','"'),
            ('qpetikbutton','"','"') : ('qatrbutton' , '"','ε'),

            ('qatrbutton','s','X') : ('qstylebutton','ε', 's'),
            ('qstylebutton','t','s') : ('qstylebutton','ε','t'),
            ('qstylebutton','y','t') : ('qstylebutton','ε','y'),
            ('qstylebutton','l','y') : ('qstylebutton','y','ε'),
            ('qstylebutton','e','t') : ('qstylebutton','t','ε'),
            ('qstylebutton','=','s') : ('qstylebutton','s','ε'),
            ('qstylebutton','"','X') : ('qpetikbutton','ε','"'),
            ('qpetikbutton','"','"') : ('qatrbutton' , '"','ε'),
   
            ('qatrbutton','i','X') : ('qidbutton','ε', 'i'),
            ('qidbutton','d','i') : ('qidbutton','i','ε'),
            ('qidbutton','=','X') : ('q=button','ε','ε'),
            ('q=button','"','X') : ('qpetikbutton','ε','"'),
            ('qpetikbutton','"','"') : ('qatrbutton' , '"','ε'),

            ('qatrbutton','t','X') : ('qtypebutton','ε', 't'),
            ('qtypebutton','y','t') : ('qtypebutton','ε','y'),
            ('qtypebutton','p','y') : ('qtypebutton','y','ε'),
            ('qtypebutton','e','t') : ('qtypebutton','t','ε'),
            ('qtypebutton','=','X') : ('q=button','ε','ε'),
            ('q=button','"','X') : ('qpetiktypebutton','ε','"'),
            ('qpetiktypebutton','"','"') : ('qatrbutton' , '"','ε'),

            ('qpetiktypebutton','s','"') : ('qsubmitbutton' , 'ε','s'),
            ('qsubmitbutton','u','s') : ('qsubmitbutton' , 'ε','u'),
            ('qsubmitbutton','b','u') : ('qsubmitbutton' , 'ε','b'),
            ('qsubmitbutton','m','b') : ('qsubmitbutton' , 'b','ε'), 
            ('qsubmitbutton','i','u') : ('qsubmitbutton' , 'u','ε'), 
            ('qsubmitbutton','t','s') : ('qpetiktypebutton' , 's','ε'),

            ('qpetiktypebutton','b','"') : ('qbuttonbutton' , 'ε','b'),
            ('qbuttonbutton','u','b') : ('qbuttonbutton' , 'ε','u'),
            ('qbuttonbutton','t','u') : ('qbuttonbutton' , 'ε','t'),
            ('qbuttonbutton','t','t') : ('qbuttonbutton' , 't','ε'), 
            ('qbuttonbutton','o','u') : ('qbuttonbutton' , 'u','ε'), 
            ('qbuttonbutton','n','b') : ('qpetiktypebutton' , 'b','ε'),

            ('qpetiktypebutton','r','"') : ('qresetbutton' , 'ε','r'),
            ('qresetbutton','e','r') : ('qresetbutton' , 'ε','e'),
            ('qresetbutton','s','e') : ('q=resetbutton' , 'ε','ε'),
            ('q=resetbutton','e','e') : ('qresetbutton' , 'e','ε'),  
            ('qresetbutton','t','t') : ('qpetiktypebutton' , 't','ε'),  
            #==============================endbutton===============================

            #==============================form===============================
            ('qcekbody', 'f', '>'): ('qform', 'ε', '<f'),
            ('qform', 'o', 'f'): ('qform', 'ε', 'o'),
            ('qform', 'r', 'o'): ('qform', 'ε', 'r'),
            ('qform', 'm', 'r'): ('qform', 'ε', 'm'),
            ('qform', ' ', 'm'): ('qatrform', 'ε', 'X'),
            ('qform', '>', 'm'): ('qform', 'ε', 'X>'),
            ('qatrform','>','X') :('qform', 'ε', '>'),
            ('qatrform',' ','X') : ('qatrform','ε','ε'),
            ('qform', ' ', 'X'): ('qform', 'ε', 'ε'),

            ('qform',' ','>') : ('qform','ε','ε'),
            ('qform','<','>') : ('endform','>','ε'),
            ('endform','/','X') : ('endform','X','ε'),
            ('endform','f','m') : ('endform','m','ε'),
            ('endform','o','r') : ('endform','r','ε'),
            ('endform','r','o') : ('endform','o','ε'),
            ('endform','m','f') : ('endform','f','ε'),
            ('endform','>','<') : ('qcekbody','<','ε'),

            #atribut form
            ('qatrform','c','X') : ('qclassform','ε', 'c'),
            ('qclassform','l','c') : ('qclassform','ε','l'),
            ('qclassform','a','l') : ('qclassform','ε','a'),
            ('qclassform','s','a') : ('qclassform','a','ε'),
            ('qclassform','s','l') : ('qclassform','l','ε'),
            ('qclassform','=','c') : ('qclassform','c','ε'),
            ('qclassform','"','X') : ('qpetikform','ε','"'),
            ('qpetikform','"','"') : ('qatrform' , '"','ε'),

            ('qatrform','s','X') : ('qstyleform','ε', 's'),
            ('qstyleform','t','s') : ('qstyleform','ε','t'),
            ('qstyleform','y','t') : ('qstyleform','ε','y'),
            ('qstyleform','l','y') : ('qstyleform','y','ε'),
            ('qstyleform','e','t') : ('qstyleform','t','ε'),
            ('qstyleform','=','s') : ('qstyleform','s','ε'),
            ('qstyleform','"','X') : ('qpetikform','ε','"'),
            ('qpetikform','"','"') : ('qatrform' , '"','ε'),
   
            ('qatrform','i','X') : ('qidform','ε', 'i'),
            ('qidform','d','i') : ('qidform','i','ε'),
            ('qidform','=','X') : ('q=form','ε','ε'),
            ('q=form','"','X') : ('qpetikform','ε','"'),
            ('qpetikform','"','"') : ('qatrform' , '"','ε'),

            ('qatrform','t','X') : ('qmethodform','ε', 't'),
            ('qmethodform','y','t') : ('qmethodform','ε','y'),
            ('qmethodform','p','y') : ('qmethodform','y','ε'),
            ('qmethodform','e','t') : ('qmethodform','t','ε'),
            ('qmethodform','=','X') : ('q=form','ε','ε'),
            ('q=form','"','X') : ('qpetikmethod','ε','"'),
            ('qpetikmethod','"','"') : ('qatrform' , '"','ε'),

            ('qpetikmethod','P','"') : ('qpostform' , 'ε','P'),
            ('qpostform','O','P') : ('qpostform' , 'ε','O'),
            ('qpostform','S','O') : ('qpostform' , 'O','b'), 
            ('qpostform','T','P') : ('qpetikmethod' , 'P','ε'),

            ('qpetikmethod','G','"') : ('qgetform' , 'ε','G'),
            ('qgetform','E','G') : ('q=getform' , 'ε','ε'), 
            ('q=getform','T','G') : ('qpetikmethod' , 'G','ε'),

            ('qatrform','t','X') : ('qactionform','ε', 't'),
            ('qactionform','y','t') : ('qactionform','ε','y'),
            ('qactionform','p','y') : ('qactionform','y','ε'),
            ('qactionform','e','t') : ('qactionform','t','ε'),
            ('qactionform','=','X') : ('q=form','ε','ε'),
            ('q=form','"','X') : ('qpetikform','ε','"'),
            ('qpetikform','"','"') : ('qatrform' , '"','ε'),
            #==============================endform===============================

            #================================input=============================
            ('qimg', 'n', 'i'): ('qinput', 'ε', 'n'),
            ('qinput', 'p', 'n'): ('qinput', 'n', 'ε'),
            ('qinput', 'u', 'i'): ('qinput', 'i', 'ε'),
            ('qinput', 't', '<'): ('qinput', '<', 'ε'),
            ('qinput', ' ', '>'): ('qatrinput', 'ε', 'X'),
            ('qinput', '>', '>'): ('qcekbody', 'ε', 'ε'),
            ('qatrinput','>','X') :('qcekbody', 'X', 'ε'),
            ('qatrinput',' ','X') : ('qatrinput','ε','ε'),
            ('qinput', ' ', 'X'): ('qinput', 'ε', 'ε'),

            ('qatrinput','c','X') : ('qclassinput','ε', 'c'),
            ('qclassinput','l','c') : ('qclassinput','ε','l'),
            ('qclassinput','a','l') : ('qclassinput','ε','a'),
            ('qclassinput','s','a') : ('qclassinput','a','ε'),
            ('qclassinput','s','l') : ('qclassinput','l','ε'),
            ('qclassinput','=','c') : ('qclassinput','c','ε'),
            ('qclassinput','"','X') : ('qpetikinput','ε','"'),
            ('qpetikinput','"','"') : ('qatrinput' , '"','ε'),

            ('qatrinput','s','X') : ('qstyleinput','ε', 's'),
            ('qstyleinput','t','s') : ('qstyleinput','ε','t'),
            ('qstyleinput','y','t') : ('qstyleinput','ε','y'),
            ('qstyleinput','l','y') : ('qstyleinput','y','ε'),
            ('qstyleinput','e','t') : ('qstyleinput','t','ε'),
            ('qstyleinput','=','s') : ('qstyleinput','s','ε'),
            ('qstyleinput','"','X') : ('qpetikinput','ε','"'),
            ('qpetikinput','"','"') : ('qatrinput' , '"','ε'),
   
            ('qatrinput','i','X') : ('qidinput','ε', 'i'),
            ('qidinput','d','i') : ('qidinput','i','ε'),
            ('qidinput','=','X') : ('q=input','ε','ε'),
            ('q=input','"','X') : ('qpetikinput','ε','"'),
            ('qpetikinput','"','"') : ('qatrinput' , '"','ε'),

            ('qatrinput','t','X') : ('qtypeinput','ε', 't'),
            ('qtypeinput','y','t') : ('qtypeinput','ε','y'),
            ('qtypeinput','p','y') : ('qtypeinput','y','ε'),
            ('qtypeinput','e','t') : ('qtypeinput','t','ε'),
            ('qtypeinput','=','X') : ('q=input','ε','ε'),
            ('q=input','"','X') : ('qpetiktypeinput','ε','"'),
            ('qpetiktypeinput','"','"') : ('qatrinput' , '"','ε'),

            ('qpetiktypeinput','n','"') : ('qnumberinput' , 'ε','n'),
            ('qnumberinput','u','n') : ('qnumberinput' , 'ε','u'),
            ('qnumberinput','m','u') : ('qnumberinput' , 'ε','m'),
            ('qnumberinput','b','m') : ('qnumberinput' , 'm','ε'), 
            ('qnumberinput','e','u') : ('qnumberinput' , 'u','ε'), 
            ('qnumberinput','r','n') : ('qpetiktypeinput' , 'n','ε'),

            ('qpetiktypeinput','p','"') : ('qpasswordinput' , 'ε','p'),
            ('qpasswordinput','a','p') : ('qpasswordinput' , 'ε','a'),
            ('qpasswordinput','s','a') : ('qpasswordinput' , 'ε','s'),
            ('qpasswordinput','s','s') : ('qpasswordinput' , 'ε','s'), 
            ('qpasswordinput','w','s') : ('qpasswordinput' , 's','ε'), 
            ('qpasswordinput','o','s') : ('qpasswordinput' , 's','ε'),
            ('qpasswordinput','r','a') : ('qpasswordinput' , 'a','ε'),  
            ('qpasswordinput','d','p') : ('qpetiktypeinput' , 'p','ε'),

            ('qpetiktypeinput','c','"') : ('qcheckboxinput' , 'ε','c'),
            ('qcheckboxinput','h','c') : ('qcheckboxinput' , 'ε','h'),
            ('qcheckboxinput','e','h') : ('qcheckboxinput' , 'ε','e'),
            ('qcheckboxinput','c','e') : ('qcheckboxinput' , 'ε','c'), 
            ('qcheckboxinput','k','c') : ('qcheckboxinput' , 'c','ε'), 
            ('qcheckboxinput','b','e') : ('qcheckboxinput' , 'e','ε'),
            ('qcheckboxinput','o','h') : ('qcheckboxinput' , 'h','ε'),  
            ('qcheckboxinput','x','c') : ('qpetiktypeinput' , 'c','ε'),

            ('qpetiktypeinput','t','"') : ('qtextinput' , 'ε','t'),
            ('qtextinput','e','t') : ('qtextinput' , 'ε','e'),
            ('qtextinput','x','e') : ('qtextinput' , 'e','ε'), 
            ('qtextinput','t','t') : ('qpetiktypeinput' , 't','ε'),

            ('qpetiktypeinput','e','"') : ('qemailinput' , 'ε','e'),
            ('qemailinput','m','e') : ('qemailinput' , 'ε','m'),
            ('qemailinput','a','m') : ('q=emailinput' , 'ε','ε'),
            ('q=emailinput','i','m') : ('qemailinput' , 'm','ε'), 
            ('qemailinput','l','e') : ('qpetiktypeinput' , 'e','ε'),
            #================================endinput=============================
            
            #================================table=============================
            ('qcekbody', 't', '>'): ('qtable', 'ε', '<t'),
            ('qtable', 'a', 't'): ('qtable', 'ε', 'a'),
            ('qtable', 'b', 'a'): ('qtable', 'ε', 'b'),
            ('qtable', 'l', 'b'): ('qtable', 'ε', 'l'),
            ('qtable', 'e', 'l'): ('qtable', 'ε', 'e'),
            ('qtable', ' ', 'e'): ('qatrtable', 'ε', 'X'),
            ('qtable', '>', 'e'): ('qtable', 'ε', 'X>'),
            ('qatrtable','>','X') :('qtable', 'ε', '>'),
            ('qatrtable',' ','X') : ('qatrtable','ε','ε'),
            ('qtable', ' ', 'X'): ('qtable', 'ε', 'ε'),

            ('qtable', '<', '>'): ('qcektable', 'ε', 'ε'),
            ('qcektable',' ','>') : ('qcektable','ε','ε'),

            ('qtable',' ','>') : ('qtable','ε','ε'),
            ('qcektable','/','>') : ('qcektable','>','ε'),
            ('qcektable','t','X') : ('endtable','X','ε'),
            ('endtable','a','e') : ('endtable','e','ε'),
            ('endtable','b','l') : ('endtable','l','ε'),
            ('endtable','l','b') : ('endtable','b','ε'),
            ('endtable','e','a') : ('endtable','a','ε'),
            ('endtable','>','t') : ('endtable','t','ε'),
            ('endtable',' ','<') : ('qcekbody','<','ε'),

            ('qatrtable','c','X') : ('qclasstable','ε', 'c'),
            ('qclasstable','l','c') : ('qclasstable','ε','l'),
            ('qclasstable','a','l') : ('qclasstable','ε','a'),
            ('qclasstable','s','a') : ('qclasstable','a','ε'),
            ('qclasstable','s','l') : ('qclasstable','l','ε'),
            ('qclasstable','=','c') : ('qclasstable','c','ε'),
            ('qclasstable','"','X') : ('qpetiktable','ε','"'),
            ('qpetiktable','"','"') : ('qatrtable' , '"','ε'),

            ('qatrtable','s','X') : ('qstyletable','ε', 's'),
            ('qstyletable','t','s') : ('qstyletable','ε','t'),
            ('qstyletable','y','t') : ('qstyletable','ε','y'),
            ('qstyletable','l','y') : ('qstyletable','y','ε'),
            ('qstyletable','e','t') : ('qstyletable','t','ε'),
            ('qstyletable','=','s') : ('qstyletable','s','ε'),
            ('qstyletable','"','X') : ('qpetiktable','ε','"'),
            ('qpetiktable','"','"') : ('qatrtable' , '"','ε'),
            #================================endtable=============================

            #================================tr, td, th=============================
            ('qcektable','t','>') : ('qcektable','ε','<t'),
            ('qcektable','r','t') : ('qtr','ε','r'), 
            ('qcektable','d','t') : ('qtd','ε','d'), 
            ('qcektable','h','t') : ('qth','ε','h'),
            ('qtr',' ','r') : ('qatrtr','ε','X'),
            ('qtd',' ','d') : ('qatrtd','ε','X'),
            ('qth',' ','r') : ('qatrth','ε','X'),
            ('qtr','>','r') : ('qtr','ε','X>'),
            ('qtd','>','d') : ('qtd','ε','X>'),
            ('qth','>','h') : ('qth','ε','X>'),
            ('qatrtr','>','X') : ('qtr','ε','>'),
            ('qatrtd','>','X') : ('qtd','ε','>'),
            ('qatrth','>','X') : ('qth','ε','>'),
            ('qtr','<','>') : ('endt','>','ε'),
            ('qtd','<','>') : ('endt','>','ε'),
            ('qth','<','>') : ('endt','>','ε'),

            ('qth', ' ', '>'): ('qth', 'ε', 'ε'),
            ('qtr', ' ', '>'): ('qtr', 'ε', 'ε'),
            ('qtd', ' ', '>'): ('qtd', 'ε', 'ε'),

            ('qatrth', ' ', 'X'): ('qatrth', 'ε', 'ε'),
            ('qatrtr', ' ', 'X'): ('qatrtr', 'ε', 'ε'),
            ('qatrtd', ' ', 'X'): ('qatrtd', 'ε', 'ε'),

            ('endt','/','X') : ('endt','X','ε'),
            ('endt','/','X') : ('endt','X','ε'),
            ('endt','/','X') : ('endt','X','ε'),
            ('endt','t','r') : ('endtr','r','ε'),
            ('endt','t','d') : ('endtd','d','ε'),
            ('endt','t','h') : ('endth','h','ε'),
            ('endtr','r','t') : ('endtr','t','ε'),
            ('endtd','d','t') : ('endtd','t','ε'),
            ('endth','h','t') : ('endth','t','ε'),
            ('endtr','>','<') : ('qtable','<','ε'),
            ('endtd','>','<') : ('qtable','<','ε'),
            ('endth','>','<') : ('qtable','<','ε'), 
            
            ('qatrth','c','X') : ('qclassth','ε', 'c'),
            ('qclassth','l','c') : ('qclassth','ε','l'),
            ('qclassth','a','l') : ('qclassth','ε','a'),
            ('qclassth','s','a') : ('qclassth','a','ε'),
            ('qclassth','s','l') : ('qclassth','l','ε'),
            ('qclassth','=','c') : ('qclassth','c','ε'),
            ('qclassth','"','X') : ('qpetikth','ε','"'),
            ('qpetikth','"','"') : ('qatrth' , '"','ε'),

            ('qatrth','s','X') : ('qstyleth','ε', 's'),
            ('qstyleth','t','s') : ('qstyleth','ε','t'),
            ('qstyleth','y','t') : ('qstyleth','ε','y'),
            ('qstyleth','l','y') : ('qstyleth','y','ε'),
            ('qstyleth','e','t') : ('qstyleth','t','ε'),
            ('qstyleth','=','s') : ('qstyleth','s','ε'),
            ('qstyleth','"','X') : ('qpetikth','ε','"'),
            ('qpetikth','"','"') : ('qatrth' , '"','ε'),

            ('qatrtd','c','X') : ('qclasstd','ε', 'c'),
            ('qclasstd','l','c') : ('qclasstd','ε','l'),
            ('qclasstd','a','l') : ('qclasstd','ε','a'),
            ('qclasstd','s','a') : ('qclasstd','a','ε'),
            ('qclasstd','s','l') : ('qclasstd','l','ε'),
            ('qclasstd','=','c') : ('qclasstd','c','ε'),
            ('qclasstd','"','X') : ('qpetiktd','ε','"'),
            ('qpetiktd','"','"') : ('qatrtd' , '"','ε'),

            ('qatrtd','s','X') : ('qstyletd','ε', 's'),
            ('qstyletd','t','s') : ('qstyletd','ε','t'),
            ('qstyletd','y','t') : ('qstyletd','ε','y'),
            ('qstyletd','l','y') : ('qstyletd','y','ε'),
            ('qstyletd','e','t') : ('qstyletd','t','ε'),
            ('qstyletd','=','s') : ('qstyletd','s','ε'),
            ('qstyletd','"','X') : ('qpetiktd','ε','"'),
            ('qpetiktd','"','"') : ('qatrtd' , '"','ε'),

            ('qatrtr','c','X') : ('qclasstr','ε', 'c'),
            ('qclasstr','l','c') : ('qclasstr','ε','l'),
            ('qclasstr','a','l') : ('qclasstr','ε','a'),
            ('qclasstr','s','a') : ('qclasstr','a','ε'),
            ('qclasstr','s','l') : ('qclasstr','l','ε'),
            ('qclasstr','=','c') : ('qclasstr','c','ε'),
            ('qclasstr','"','X') : ('qpetiktr','ε','"'),
            ('qpetiktr','"','"') : ('qatrtr' , '"','ε'),

            ('qatrtr','s','X') : ('qstyletr','ε', 's'),
            ('qstyletr','t','s') : ('qstyletr','ε','t'),
            ('qstyletr','y','t') : ('qstyletr','ε','y'),
            ('qstyletr','l','y') : ('qstyletr','y','ε'),
            ('qstyletr','e','t') : ('qstyletr','t','ε'),
            ('qstyletr','=','s') : ('qstyletr','s','ε'),
            ('qstyletr','"','X') : ('qpetiktr','ε','"'),
            ('qpetiktr','"','"') : ('qatrtr' , '"','ε'),

                        ('qatrth','i','X') : ('qidth','ε', 'i'),
            ('qidth','d','i') : ('qidth','i','ε'),
            ('qidth','=','X') : ('q=th','ε','ε'),
            ('q=th','"','X') : ('qpetikth','ε','"'),
            ('qpetikth','"','"') : ('qatrth' , '"','ε'),

            ('qatrtd','i','X') : ('qidtd','ε', 'i'),
            ('qidtd','d','i') : ('qidtd','i','ε'),
            ('qidtd','=','X') : ('q=td','ε','ε'),
            ('q=td','"','X') : ('qpetiktd','ε','"'),
            ('qpetiktd','"','"') : ('qatrtd' , '"','ε'),

            ('qatrtr','i','X') : ('qidtr','ε', 'i'),
            ('qidtr','d','i') : ('qidtr','i','ε'),
            ('qidtr','=','X') : ('q=tr','ε','ε'),
            ('q=tr','"','X') : ('qpetiktr','ε','"'),
            ('qpetiktr','"','"') : ('qatrtr' , '"','ε'),
           
         
}

#==========================BACA FILE ======================#

# filename = 'src//rules.txt'

# with open(filename, 'r') as file:
#     content = file.read()

# exec(content)

# print("States:", states)
# print("Input Alphabet:", input_alphabet)
# print("Stack Alphabet:", stack_alphabet)
# print("Transitions:", transition)



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

result_string = ""
inside_tag = False

for char in html_content:
    if char == '<':
        inside_tag = True
        result_string += ' ' + char
    elif char == '>':
        inside_tag = False
        result_string += char + ' '
    else:
        result_string += char
# Sekarang, variabel html_content berisi seluruh string dari file HTML

result_string = " ".join(result_string.split())


#======================================CREATE FILE======================#
with open('src//rules.txt', 'w', encoding='utf-8') as file:
    file.write("states = " + str(states) + "\n")
    file.write("input_alphabet = " + str(input_alphabet) + "\n")
    file.write("stack_alphabet = " + str(stack_alphabet) + "\n")
    file.write("transition = {\n")
    for rule in transition:
        file.write(f"    {rule}: {transition[rule]},\n")
    file.write("}\n")

print(result_string)

result = pda.process_input(result_string)

if result:
    print(f"Input '{result_string}' is accepted.")
else:
    print(f"Input '{result_string}' is not accepted.")
