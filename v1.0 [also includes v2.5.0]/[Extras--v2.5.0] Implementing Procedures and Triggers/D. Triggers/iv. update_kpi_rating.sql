DELIMITER $$
CREATE TRIGGER update_kpi_rating
AFTER INSERT ON Performance
FOR EACH ROW
BEGIN
    UPDATE Projects
    SET kpi_rating = (
        SELECT AVG((on_time_completion + quality_of_work + team_contribution) / 3)
        FROM Performance
        WHERE project_id = NEW.project_id
    )
    WHERE project_id = NEW.project_id;
END $$
DELIMITER ;
