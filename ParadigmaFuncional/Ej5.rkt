#lang racket

; sin simplificar
(define a 3)
(define b 2)
(define c 1)
(+ (/ (* 7 a) b) (/ (* 3 a) b) (/ (* 7 a) b))
(cons (car (list a b c)) (cdr (list a b c)))

; simplificado con let
(let ([exp1 (/ (* 7 a) b)]
      [exp2 (/ (* 3 a) b)])
  (+ exp1 exp2 exp1))

(let ([lst (list a b c)])
  (cons (car lst) (cdr lst)))