fun main() {
    val signalcase_1 = Signal(74, 89, 13, 8, 7)
    check(Policy.score(signalcase_1) == 165)
    check(Policy.classify(signalcase_1) == "review")
    val signalcase_2 = Signal(90, 73, 21, 20, 10)
    check(Policy.score(signalcase_2) == 89)
    check(Policy.classify(signalcase_2) == "review")
    val signalcase_3 = Signal(89, 72, 13, 6, 6)
    check(Policy.score(signalcase_3) == 186)
    check(Policy.classify(signalcase_3) == "accept")
}
