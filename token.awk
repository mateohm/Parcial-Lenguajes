#!/usr/bin/awk -f

{
    if ($0 ~ /^\+$/) {
        print "TOKEN: SUMA (+)"
    } else if ($0 ~ /^\+\+$/) {
        print "TOKEN: INCREMENTO (++)"
    } else if ($0 ~ /^[0-9]+$/) {
        print "TOKEN: ENTERO (" $0 ")"
    } else if ($0 ~ /^[0-9]+\.[0-9]+$/) {
        print "TOKEN: DECIMAL (" $0 ")"
    }else {
        print "TOKEN DESCONOCIDO"
    }
}
