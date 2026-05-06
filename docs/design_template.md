# Design Template

## Problem

Hệ thống cần xử lý: Tìm kiếm thông tin, tổng hợp, phân tích và trả lời câu hỏi dài.

## Why multi-agent?

Single agent dễ bị mất focus khi câu hỏi quá dài và cần nhiều bước suy luận, thu thập thông tin. Multi-agent chia nhỏ vấn đề.

## Agent roles

| Agent | Responsibility | Input | Output | Failure mode |
|---|---|---|---|---|
| Supervisor | Điều phối workflow | State | State cập nhật route | Lặp vô hạn |
| Researcher | Tìm kiếm tài liệu | Query | Sources, notes | Không tìm thấy tài liệu |
| Analyst | Phân tích thông tin | Sources, notes | Analysis notes | Phân tích sai |
| Writer | Viết bài trả lời | Analysis notes | Final answer | Viết lan man, thiếu cite |

## Shared state

Các fields chính: `query`, `route_history`, `sources`, `research_notes`, `analysis_notes`, `final_answer`.

## Routing policy

Workflow tuần tự: Supervisor -> Researcher -> Analyst -> Writer -> Supervisor (done).

## Guardrails

- Max iterations: 5
- Timeout: 60s
- Retry: 3
- Fallback: Trả về lỗi nếu fail
- Validation: Schema Pydantic

## Benchmark plan

So sánh Quality, Latency, Cost giữa Single-agent và Multi-agent.