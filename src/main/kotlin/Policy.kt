data class Signal(val demand: Int, val capacity: Int, val latency: Int, val risk: Int, val weight: Int)

object Policy {
    private const val threshold = 176
    private const val riskPenalty = 6
    private const val latencyPenalty = 4
    private const val weightBonus = 4

    fun score(signal: Signal): Int =
        signal.demand * 2 + signal.capacity + signal.weight * weightBonus -
            signal.latency * latencyPenalty - signal.risk * riskPenalty

    fun classify(signal: Signal): String = if (score(signal) >= threshold) "accept" else "review"
}
