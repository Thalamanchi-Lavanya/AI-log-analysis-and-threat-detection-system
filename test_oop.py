from analyzer.threat_detector_oop import ThreatDetector

detector = ThreatDetector(
    "AI Threat Detection System"
)

detector.welcome()

detector.analyze_log(
    "logs/test.log"
)