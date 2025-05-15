from django.db import models
from django.contrib.auth.models import User

class Workspace(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='workspaces'
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"


class LinkStatus(models.TextChoices):
    ALIVE = 'alive', 'Alive'
    REDIRECTED = 'redirected', 'Redirected'
    DEAD = 'dead', 'Dead'


class Bookmark(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bookmarks'
    )
    name = models.CharField(max_length=200)
    link = models.URLField()
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=10,
        choices=LinkStatus.choices,
        default=LinkStatus.ALIVE,
    )
    created = models.DateTimeField(auto_now_add=True)

    workspaces = models.ManyToManyField(
        Workspace,
        through='WorkspaceBookmark',
        related_name='bookmarks',
        blank=True
    )
    tags = models.ManyToManyField(
        'Tag',
        through='BookmarkTag',
        related_name='bookmarks',
        blank=True
    )

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tags'
    )
    

    def __str__(self):
        return self.name


class BookmarkTag(models.Model):
    bookmark = models.ForeignKey(
        Bookmark,
        on_delete=models.CASCADE
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('bookmark', 'tag')

    def __str__(self):
        return f"{self.bookmark.name} → {self.tag.name}"


class WorkspaceBookmark(models.Model):
    bookmark = models.ForeignKey(
        Bookmark,
        on_delete=models.CASCADE
    )
    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('workspace', 'bookmark')

    def __str__(self):
        return f"{self.bookmark.name} in {self.workspace.name}"