#lang racket

(define (convdatos (l '()))
    (define (conv l)
        (if (null? l)
            null
            (if (string? (car l))
                (if (equal? (car l) "F")
                    (cons 0 (conv (cdr l)))
                    (if (equal? (car l) "V")
                        (cons 1 (conv (cdr l))) 
                        (if (number? (string->number (car l)))
                            (cons (string->number (car l)) (conv (cdr l)))
                            null
                        )
                    )
                )
                (if (number? (car l))
                    (cons (car l) (conv (cdr l))) 
                    (if (symbol? (car l))
                        (if (equal? (car l) 'F)
                            (cons 0 (conv (cdr l)))
                            (if (equal? (car l) 'V)
                                (cons 1 (conv (cdr l))) 
                                null
                            )
                        )
                        null
                    )
                )
                
            )     
        ) 
    )
    (if (null? l)
        null 
        (cons (conv (car (cdr (car l)))) (convdatos (cdr l)))
    )
)

(convdatos (list (list "N" (list 1 2 3)) (list "B" (list 'V 'F)) (list "S" (list "0" "1" "3"))))