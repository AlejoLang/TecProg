#lang racket
(define lst '(a b c . x))
(define lst2 '(a b c x))
(define lst3 '((a . x) b))
(define lst4 '(x . a))
(define lst5 '(a . x))

(cdr (cdr (cdr lst)))
(cdr (cdr (cdr lst)))
(car (cdr (cdr (cdr lst2))))
(cdr (car lst3))
(car lst4)
(cdr lst5)
