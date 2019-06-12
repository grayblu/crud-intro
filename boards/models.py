from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail


# Create your models here.
class Board(models.Model):
    # id (pk) 는 기본적으로 처음 테이블 생성시 자동 생성된다.
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = ProcessedImageField(
        upload_to='boards/images',   # 저장 위치 (media 이후의 경로)
        processors=[Thumbnail(200,300)],    # 처리할 작업 목록
        format='JPEG',  # 저장 포맷
        options={'quality': 90},    # 추가 옵션
    )
    # image = models.ImageField(blank=True)     # 새로운 컬럼 추가 시 테이블 가장 오른쪽에 배치됨, 이미지 없이도 게시 가능
    # auto_now_add : 생성일자 / db 가 최초 저장시에만 적용
    # auto_now : 수정일자 / db가 새로 저장될때마다 갱신
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}글 - {self.title}: {self.content}'


class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return self.content
        return f'<Board({self.board_id}): Comment({self.pk, self.content}>'

