from os import getcwd
from time import time
from pathlib import Path
from requests import Session, Response

class RandomDuk:
	def __init__(self) -> None:
		self.api = "https://random-d.uk/api"
		self.session = Session()
		self.session.headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}

	def _get(self, endpoint: str) -> Response:
		return self.session.post(f"{self.api}{endpoint}")

	def save_file(
			self,
			content: bytes,
			location: str = getcwd()) -> bool:
		with open(
				Path(location).joinpath(f"{time() * 1000}.jpg"), mode="wb+") as file:
			file.write(content)
		return True

	def get_random_image_url(self) -> dict:
		return self._get("/random").json()

	def get_random_image(self) -> bool:
		return save_file(self._get("/random").content)

	def get_all_images(self) -> dict:
		return self._get("/list").json()

	def get_image(self, image_number: int) -> bool:
		return save_file(self._get(f"/{image_number}.jpg").content)

	def get_gif(self, gif_number: int) -> bool:
		return save_file(self._get(f"/{gif_number}").content)
