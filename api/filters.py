import uuid

import django_filters

from articles.models import Article, Tag


class ArticleFilter(django_filters.FilterSet):
    is_favorited = django_filters.BooleanFilter(label='Статья в избранном')
    tags = django_filters.filters.ModelMultipleChoiceFilter(
        queryset=Tag.objects.all(),
        method='filter_tags',
        label='Статьи по указанным тегам',
    )
    tags_exclude = django_filters.filters.ModelMultipleChoiceFilter(
        queryset=Tag.objects.all(),
        method='filter_tags_exclude',
        label='Статьи без указанных тегов',
    )

    class Meta:
        model = Article
        fields = ()

    @staticmethod
    def _filter_articles_by_tags(tags, queryset, filtering_method):
        """Фильтр переданного queryset по тегам методом filtering_method."""
        tag_subtrees = []
        tag_found = False
        for tag in tags:
            for tag_subtree in tag_subtrees:
                if tag in tag_subtree:
                    tag_found = True
                    break
            if not tag_found:
                t_subtree = tag.get_descendants(include_self=True)
                tag_subtrees.append(t_subtree)
                queryset = getattr(queryset, filtering_method)(tags__in=t_subtree)
            tag_found = False
        return queryset

    def filter_tags(self, queryset, name, value: list[uuid.UUID]):  # noqa: WPS122
        """Фильтрует articles, выбирая статьи с указанными тегами."""
        if not value:
            return queryset
        return self._filter_articles_by_tags(value, queryset, 'filter')

    def filter_tags_exclude(  # noqa: WPS122
        self,
        queryset,
        name,
        value: list[uuid.UUID],
    ):
        """Фильтрует articles, исключая статьи с указанными тегами."""
        if not value:
            return queryset
        return self._filter_articles_by_tags(value, queryset, 'exclude')
