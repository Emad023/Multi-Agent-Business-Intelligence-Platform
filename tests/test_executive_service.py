from services.executive_service import (
    generate_executive_summary
)

summary = generate_executive_summary()

for section, data in summary.items():
    print("\n" + "="*50)
    print(section.upper())
    print("="*50)
    print(data)