#lang racket

(define (count-elem p x [n 0])
    (if (null? x)
        n
        (if (= (car x) p)
            (count-elem p (cdr x) (+ n 1))
            (count-elem p (cdr x) n)
        )
    )
)

(count-elem 3 '(1 2 3 4 5 4 3 2 1))
