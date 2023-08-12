export function secondsToTimestamp(seconds: number) {
	const hours = Math.floor(seconds / 3600);
	const minutes = Math.floor((seconds - hours * 3600) / 60);
	const seconds_ = Math.floor(seconds - hours * 3600 - minutes * 60);
	const hours_str = hours < 10 ? '0' + hours : hours;
	const minutes_str = minutes < 10 ? '0' + minutes : minutes;
	const seconds_str = seconds_ < 10 ? '0' + seconds_ : seconds_;
	return `${hours_str}:${minutes_str}:${seconds_str}`;
}
