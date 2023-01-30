export interface ISchedule {
  id: number;
  coach_id: number;
  student_id: number;
  begin_time: string;
  end_time: string;
}

export interface IFeedbackResponse {
  schedule_id: number;
  rating: number;
  notes: string;
}
