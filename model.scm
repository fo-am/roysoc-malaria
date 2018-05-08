#lang racket
(require plot)

(define lifespan (* 70 365))
(define D 30)
(define beta 1)
(define R0 (/ beta (+ (/ 1 lifespan) (/ 1 D))))

(define (predY P phiD phiB beta)
  (let ((mu (/ 1 lifespan)))
    (max 0 (* mu (- (* (- 1 P) (- 1 phiD) D)
                    (/ 1 (* (- 1.000001 phiB) beta)))))))

(plot (function (lambda (x) (predY x 0 0 1)) 0 1)
      #:x-label "vaccination effort" #:y-label "predicted Y")
(plot (function (lambda (x) (predY 0 x 0 1)) 0 1)
      #:x-label "drugs effort" #:y-label "predicted Y")
(plot (function (lambda (x) (predY 0 0 x 1)) 0 1)
      #:x-label "bednets effort" #:y-label "predicted Y")

(plot3d (surface3d (lambda (x y) (predY 0 x y 1)) 0 1 0 1)
      #:x-label "drugs effort" #:y-label "bednets effort")
(plot3d (surface3d (lambda (x y) (predY y x 0 1)) 0 1 0 1)
      #:x-label "drugs effort" #:y-label "vaccination effort")
(plot3d (surface3d (lambda (x y) (predY y x 0 50)) 0 1 0 1)
      #:x-label "drugs effort" #:y-label "vaccination effort")
