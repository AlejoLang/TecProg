#lang racket

(struct point (x y))

(define (distance p1 p2)
    (sqrt (+ (sqr (- (point-x p1) (point-x p2))) (sqr (- (point-y p1) (point-y p2)))))
)

(distance (point 1 1) (point 0 0))
(distance (point 3 4) (point 0 0))