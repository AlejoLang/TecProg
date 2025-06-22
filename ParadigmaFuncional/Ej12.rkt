#lang racket
(define (subst p r x)
    (if (null? x)
        x
        (if (eq? (car x) p)
            (cons r (subst p r (cdr x)))
            (cons (car x) (subst p r (cdr x)))
        )
    )
)

(subst 'c 'k '( c o c o n u t))