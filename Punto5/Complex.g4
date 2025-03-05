grammar Complex;

expr: expr ('+'|'-') expr 
    | expr ('*'|'/') expr 
    | '(' expr ')' 
    | complex
    ;

complex: NUM ('+'|'-') NUM 'i' | NUM 'i' ;

NUM: [0-9]+ ('.' [0-9]+)? ;

WS: [ \t\n\r]+ -> skip;
