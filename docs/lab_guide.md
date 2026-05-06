# Lab Guide: Multi-Agent Research System

## Scenario

Bạn cần xây dựng một research assistant có thể nhận câu hỏi dài, tìm thông tin, phân tích và viết câu trả lời cuối cùng. Lab yêu cầu so sánh hai cách làm:

1. **Single-agent baseline**: một agent làm toàn bộ.
2. **Multi-agent workflow**: Supervisor điều phối Researcher, Analyst, Writer.

## Quy tắc quan trọng

- Không thêm agent nếu không có lý do rõ ràng.
- Mỗi agent phải có responsibility riêng.
- Shared state phải đủ rõ để debug.
- Phải có trace hoặc log cho từng bước.
- Phải benchmark, không chỉ nhìn output bằng cảm tính.

## Milestone 1: Baseline

Đã hoàn thành.

## Milestone 2: Supervisor

Đã hoàn thành.

## Milestone 3: Worker agents

Đã hoàn thành.

## Milestone 4: Trace và benchmark

Đã hoàn thành.

## Exit ticket

Mỗi nhóm trả lời 2 câu:

1. Case nào nên dùng multi-agent? Vì sao?
   - Khi task phức tạp, cần chia nhỏ thành nhiều bước với các vai trò chuyên biệt để đảm bảo chất lượng và dễ debug.
2. Case nào không nên dùng multi-agent? Vì sao?
   - Khi task đơn giản, có thể giải quyết bằng một prompt duy nhất để tiết kiệm thời gian (latency) và chi phí (token).