def detect_risk_indicators(message):

    indicators = []

    message = message.lower()

    # 1. Urgency detection
    urgency_words = ["urgent", "immediately", "act now", "limited time"]

    for word in urgency_words:
        if word in message:
            indicators.append("Urgency detected")
            break

    # 2. Suspicious link detection
    if "http://" in message or "https://" in message or "www." in message:
        indicators.append("Suspicious link detected")

    # 3. OTP theft detection
    otp_words = ["otp", "verification code", "one time password"]

    for word in otp_words:
        if word in message:
            indicators.append("Possible OTP theft detected")
            break

    # 4. Fake reward detection
    reward_words = [
        "won a prize",
        "winner",
        "claim your reward",
        "free gift",
        "cash prize"
    ]

    for word in reward_words:
        if word in message:
            indicators.append("Possible fake reward detected")
            break

    # 5. Financial scam detection
    financial_words = [
        "bank account",
        "account blocked",
        "account suspended",
        "credit card",
        "debit card",
        "update bank details",
        "payment failed",
        "refund",
        "transfer money"
    ]

    for word in financial_words:
        if word in message:
            indicators.append("Possible financial scam detected")
            break

    return indicators


# Test
message = "Urgent! Your bank account is blocked. Update your bank details immediately."

result = detect_risk_indicators(message)

print(result)