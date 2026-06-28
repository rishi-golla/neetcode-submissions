class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += s + "x1f"

        return result

    def decode(self, s: str) -> List[str]:
        return s.split("x1f")[:-1]
      