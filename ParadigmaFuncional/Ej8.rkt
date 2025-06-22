#lang racket
(define pi 3.14159265358979323846)
(define (area r)
   (* pi (* r r)) 
)

(area 5)
(area 3)