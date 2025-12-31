import re


def luhn_ok(pan: str) -> bool:
    pan = re.sub(r"\D", "", pan)
    if not pan:
        return False
    s = 0
    alt = False
    for ch in reversed(pan):
        d = int(ch)
        if alt:
            d *= 2
            if d > 9:
                d -= 9
        s += d
        alt = not alt
    return s % 10 == 0


def network(pan: str) -> str:
    pan = re.sub(r"\D", "", pan)
    if pan.startswith("4"):
        return "Visa"
    if pan[:2] in {"34", "37"}:
        return "AmEx"
    if pan[:2].isdigit() and 51 <= int(pan[:2]) <= 55:
        return "Mastercard"
    if len(pan) >= 4 and pan[:4].isdigit() and 2221 <= int(pan[:4]) <= 2720:
        return "Mastercard"
    if pan.startswith("6"):
        return "Discover/UnionPay(需BIN細分)"
    return "Unknown"


def mask(pan: str, keep_bin: int = 8, keep_last: int = 4) -> str:
    pan = re.sub(r"\D", "", pan)
    if len(pan) <= keep_bin + keep_last:
        return pan
    return pan[:keep_bin] + "X" * (len(pan) - keep_bin - keep_last) + pan[-keep_last:]


def main() -> None:
    pans = (
        "5242555958046336 4477578783737704 4016060009794015 4987300419256105 "
        "4162057025377009 4380456744088408 4705380522940341 4705380347694248 "
        "4477578754874031 4213330025767530 4705380522940341 4182308704866887 "
        "4705380321802114 4213330030370171 4040080808034488"
    ).split()

    for pan in pans:
        pan_digits = re.sub(r"\D", "", pan)
        if not pan_digits:
            continue
        print(
            {
                "masked": mask(pan_digits),
                "network": network(pan_digits),
                "length": len(pan_digits),
                "luhn_ok": luhn_ok(pan_digits),
            }
        )


if __name__ == "__main__":
    main()
