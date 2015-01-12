from django.core.urlresolvers import reverse
from reviewboard.reviews.models import Comment, \
                                       DefaultReviewer, \
                                       Group, \
                                       ReviewRequest, \
                                       ReviewRequestDraft, \
                                       Review, \
                                       Screenshot
from reviewboard.testing.testcase import TestCase
    fixtures = ['test_users', 'test_reviewrequests', 'test_scmtools',
                'test_site']
            ReviewRequest.objects.public(
                user=User.objects.get(username="doc")), [
            "Comments Improvements",
            "Update for cleaned_data changes",
            "Add permission checking for JSON API",
            "Made e-mail improvements",
            "Error dialog",
            "Interdiff Revision Test",
        ])
            ReviewRequest.objects.public(status=None), [
            "Update for cleaned_data changes",
            "Add permission checking for JSON API",
            "Made e-mail improvements",
            "Error dialog",
            "Improved login form",
            "Interdiff Revision Test",
        ])
            ReviewRequest.objects.public(
                user=User.objects.get(username="doc"), status=None), [
            "Comments Improvements",
            "Update for cleaned_data changes",
            "Add permission checking for JSON API",
            "Made e-mail improvements",
            "Error dialog",
            "Improved login form",
            "Interdiff Revision Test",
        ])
        ReviewRequest.objects.all().delete()

        ReviewRequest.objects.all().delete()

        ReviewRequest.objects.all().delete()

        ReviewRequest.objects.all().delete()

        ReviewRequest.objects.all().delete()

        ReviewRequest.objects.all().delete()

        ReviewRequest.objects.all().delete()

        ReviewRequest.objects.all().delete()

        ReviewRequest.objects.all().delete()

        ReviewRequest.objects.all().delete()

        ReviewRequest.objects.all().delete()

            ["Add permission checking for JSON API"])
            ["Add permission checking for JSON API"])
            ["Update for cleaned_data changes",
             "Add permission checking for JSON API"])
            ReviewRequest.objects.to_user_groups("doc", status=None,
                local_site=None),
            ["Update for cleaned_data changes",
             "Add permission checking for JSON API"])
            ReviewRequest.objects.to_user_groups("doc",
                User.objects.get(username="doc"), local_site=None),
            ["Comments Improvements",
             "Update for cleaned_data changes",
             "Add permission checking for JSON API"])
            ["Add permission checking for JSON API",
             "Made e-mail improvements"])
            ["Add permission checking for JSON API",
             "Made e-mail improvements",
             "Improved login form"])
            ReviewRequest.objects.to_user_directly("doc",
                User.objects.get(username="doc"), status=None, local_site=None),
            ["Add permission checking for JSON API",
             "Made e-mail improvements",
             "Improved login form"])
            ReviewRequest.objects.from_user("doc", local_site=None), [])
            ReviewRequest.objects.from_user("doc", status=None, local_site=None),
            ["Improved login form"])
            ReviewRequest.objects.from_user("doc",
                user=User.objects.get(username="doc"), status=None,
                local_site=None),
            ["Comments Improvements",
             "Improved login form"])
            ReviewRequest.objects.to_user("doc", local_site=None), [
            "Update for cleaned_data changes",
            "Add permission checking for JSON API",
            "Made e-mail improvements"
        ])
            ReviewRequest.objects.to_user("doc", status=None, local_site=None), [

            "Update for cleaned_data changes",
            "Add permission checking for JSON API",
            "Made e-mail improvements",
            "Improved login form"
        ])
            ReviewRequest.objects.to_user("doc",
                User.objects.get(username="doc"), status=None, local_site=None), [
            "Comments Improvements",
            "Update for cleaned_data changes",
            "Add permission checking for JSON API",
            "Made e-mail improvements",
            "Improved login form"
        ])
        print review_requests
            self.assert_(summary in summaries,
                         u'summary "%s" not found in summary list' % summary)
            self.assert_(summary in r_summaries,
                         u'summary "%s" not found in review request list' %
                         summary)
class ReviewRequestTests(TestCase):
    fixtures = ['test_users', 'test_reviewrequests', 'test_scmtools',
                'test_site']
    def getContextVar(self, response, varname):
    def testReviewDetail0(self):
        """Testing review_detail redirect"""
    def testReviewDetail1(self):
        """Testing review_detail view (1)"""
        review_request = ReviewRequest.objects.public()[0]
        request = self.getContextVar(response, 'review_request')
    def testReviewDetail2(self):
        """Testing review_detail view (3)"""
        response = self.client.get('/r/3/')
        self.assertEqual(response.status_code, 200)
        request = self.getContextVar(response, 'review_request')
        self.assertEqual(request.submitter.username, 'admin')
        self.assertEqual(request.summary, 'Add permission checking for JSON API')
        self.assertEqual(request.description,
                         'Added some user permissions checking for JSON API functions.')
        self.assertEqual(request.testing_done, 'Tested some functions.')
        self.assertEqual(request.target_people.count(), 2)
        self.assertEqual(request.target_people.all()[0].username, 'doc')
        self.assertEqual(request.target_people.all()[1].username, 'dopey')
        self.assertEqual(request.target_groups.count(), 1)
        self.assertEqual(request.target_groups.all()[0].name, 'privgroup')

        self.assertEqual(request.bugs_closed, '1234, 5678, 8765, 4321')
        self.assertEqual(request.status, 'P')

        # TODO - diff
        # TODO - reviews

        self.client.logout()
        """Testing order of diff comments on a review."""
        review_request = ReviewRequest.objects.get(
            summary="Add permission checking for JSON API")
        filediff = \
            review_request.diffset_history.diffsets.latest().files.all()[0]

        # Remove all the reviews on this.
        review_request.reviews.all().delete()
        main_review = Review.objects.create(review_request=review_request,
                                            user=user1)
        main_comment = main_review.comments.create(filediff=filediff,
                                                   first_line=1,
                                                   num_lines=1,
                                                   text=comment_text_1)
        reply1 = Review.objects.create(review_request=review_request,
                                       user=user1,
                                       base_reply_to=main_review,
                                       timestamp=main_review.timestamp +
                                                 timedelta(days=1))
        reply1.comments.create(filediff=filediff,
                               first_line=1,
                               num_lines=1,
                               text=comment_text_2,
                               reply_to=main_comment)
        reply2 = Review.objects.create(review_request=review_request,
                                       user=user2,
                                       base_reply_to=main_review,
                                       timestamp=main_review.timestamp +
                                                 timedelta(days=2))
        reply2.comments.create(filediff=filediff,
                               first_line=1,
                               num_lines=1,
                               text=comment_text_3,
                               reply_to=main_comment)
    def testReviewDetailSitewideLogin(self):
    def testNewReviewRequest0(self):
        """Testing new_review_request view (basic responses)"""
        self.client.logout()

    def testNewReviewRequest1(self):
        """Testing new_review_request view (uploading diffs)"""
        self.client.login(username='grumpy', password='grumpy')

        response = self.client.get('/r/new/')
        self.assertEqual(response.status_code, 200)

        testdata_dir = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'scmtools', 'testdata')
        svn_repo_path = os.path.join(testdata_dir, 'svn_repo')

        repository = Repository(name='Subversion SVN',
                                path='file://' + svn_repo_path,
                                tool=Tool.objects.get(name='Subversion'))
        repository.save()

        diff_filename = os.path.join(testdata_dir, 'svn_makefile.diff')

        f = open(diff_filename, 'r')

        response = self.client.post('/r/new/', {
            'repository': repository.id,
            'diff_path': f,
            'basedir': '/trunk',
        })

        f.close()

        self.assertEqual(response.status_code, 302)

        r = ReviewRequest.objects.order_by('-time_added')[0]
        self.assertEqual(response['Location'],
                         'http://testserver%s' % r.get_absolute_url())

    def testReviewList(self):
        """Testing all_review_requests view"""
        self.client.login(username='grumpy', password='grumpy')

        response = self.client.get('/r/')
        self.assertEqual(response.status_code, 200)

        datagrid = self.getContextVar(response, 'datagrid')
        self.assert_(datagrid)
        self.assertEqual(len(datagrid.rows), 6)
        self.assertEqual(datagrid.rows[0]['object'].summary,
                         'Interdiff Revision Test')
        self.assertEqual(datagrid.rows[1]['object'].summary,
                         'Made e-mail improvements')
        self.assertEqual(datagrid.rows[2]['object'].summary,
                         'Improved login form')
        self.assertEqual(datagrid.rows[3]['object'].summary,
                         'Error dialog')
        self.assertEqual(datagrid.rows[4]['object'].summary,
                         'Update for cleaned_data changes')
        self.assertEqual(datagrid.rows[5]['object'].summary,
                         'Add permission checking for JSON API')

        self.client.logout()

    def testReviewListSitewideLogin(self):
        """Testing all_review_requests view with site-wide login enabled"""
        self.siteconfig.set("auth_require_sitewide_login", True)
        self.siteconfig.save()
        response = self.client.get('/r/')
        self.assertEqual(response.status_code, 302)

    @add_fixtures(['test_scmtools'])
    def test_all_review_requests_with_private_review_requests(self):
        """Testing all_review_requests view with private review requests"""
        ReviewRequest.objects.all().delete()

        user = User.objects.get(username='grumpy')

        # These are public
        self.create_review_request(summary='Test 1', publish=True)
        self.create_review_request(summary='Test 2', publish=True)

        repository1 = self.create_repository(public=False)
        repository1.users.add(user)
        self.create_review_request(summary='Test 3',
                                   repository=repository1,
                                   publish=True)

        group1 = self.create_review_group(invite_only=True)
        group1.users.add(user)
        review_request = self.create_review_request(summary='Test 4',
                                                    publish=True)
        review_request.target_groups.add(group1)

        # These are private
        repository2 = self.create_repository(public=False)
        self.create_review_request(summary='Test 5',
                                   repository=repository2,
                                   publish=True)

        group2 = self.create_review_group(invite_only=True)
        review_request = self.create_review_request(summary='Test 6',
                                                    publish=True)
        review_request.target_groups.add(group2)

        # Log in and check what we get.
        self.client.login(username='grumpy', password='grumpy')

        response = self.client.get('/r/')
        self.assertEqual(response.status_code, 200)

        datagrid = self.getContextVar(response, 'datagrid')
        self.assertTrue(datagrid)
        self.assertEqual(len(datagrid.rows), 4)
        self.assertEqual(datagrid.rows[0]['object'].summary, 'Test 4')
        self.assertEqual(datagrid.rows[1]['object'].summary, 'Test 3')
        self.assertEqual(datagrid.rows[2]['object'].summary, 'Test 2')
        self.assertEqual(datagrid.rows[3]['object'].summary, 'Test 1')

    def testSubmitterList(self):
        """Testing submitter_list view"""
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)

        datagrid = self.getContextVar(response, 'datagrid')
        self.assert_(datagrid)
        self.assertEqual(len(datagrid.rows), 4)
        self.assertEqual(datagrid.rows[0]['object'].username, 'admin')
        self.assertEqual(datagrid.rows[1]['object'].username, 'doc')
        self.assertEqual(datagrid.rows[2]['object'].username, 'dopey')
        self.assertEqual(datagrid.rows[3]['object'].username, 'grumpy')

    def testSubmitterListSitewideLogin(self):
        """Testing submitter_list view with site-wide login enabled"""
        self.siteconfig.set("auth_require_sitewide_login", True)
        self.siteconfig.save()
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 302)

    def testSubmitterListChars(self):
        """Testing the submitter list with various characters in the username"""
        # Test if this throws an exception. Bug #1250
        reverse('user', args=['user@example.com'])

    def test_submitter_review_requests_with_private(self):
        """Testing submitter page view with private review requests"""
        ReviewRequest.objects.all().delete()

        user = User.objects.get(username='grumpy')
        user.review_groups.clear()

        group1 = Group.objects.create(name='test-group-1')
        group1.users.add(user)

        group2 = Group.objects.create(name='test-group-2', invite_only=True)
        group2.users.add(user)

        self.create_review_request(summary='Summary 1', submitter=user,
                                   publish=True)

        review_request = self.create_review_request(summary='Summary 2',
                                                    submitter=user,
                                                    publish=True)
        review_request.target_groups.add(group2)

        response = self.client.get('/users/grumpy/')
        self.assertEqual(response.status_code, 200)

        datagrid = self.getContextVar(response, 'datagrid')
        self.assertIsNotNone(datagrid)
        self.assertEqual(len(datagrid.rows), 1)
        self.assertEqual(datagrid.rows[0]['object'].summary, 'Summary 1')

        groups = self.getContextVar(response, 'groups')
        self.assertEqual(len(groups), 1)
        self.assertEqual(groups[0], group1)

    def testGroupList(self):
        """Testing group_list view"""
        response = self.client.get('/groups/')
        self.assertEqual(response.status_code, 200)

        datagrid = self.getContextVar(response, 'datagrid')
        self.assert_(datagrid)
        self.assertEqual(len(datagrid.rows), 4)
        self.assertEqual(datagrid.rows[0]['object'].name, 'devgroup')
        self.assertEqual(datagrid.rows[1]['object'].name, 'emptygroup')
        self.assertEqual(datagrid.rows[2]['object'].name, 'newgroup')
        self.assertEqual(datagrid.rows[3]['object'].name, 'privgroup')

    def testGroupListSitewideLogin(self):
        """Testing group_list view with site-wide login enabled"""
        self.siteconfig.set("auth_require_sitewide_login", True)
        self.siteconfig.save()
        response = self.client.get('/groups/')
        self.assertEqual(response.status_code, 302)

    def testDashboard1(self):
        """Testing dashboard view (incoming)"""
        self.client.login(username='doc', password='doc')

        response = self.client.get('/dashboard/', {'view': 'incoming'})
        self.assertEqual(response.status_code, 200)

        datagrid = self.getContextVar(response, 'datagrid')
        self.assert_(datagrid)
        self.assertEqual(len(datagrid.rows), 4)
        self.assertEqual(datagrid.rows[0]['object'].summary,
                         'Made e-mail improvements')
        self.assertEqual(datagrid.rows[1]['object'].summary,
                         'Update for cleaned_data changes')
        self.assertEqual(datagrid.rows[2]['object'].summary,
                         'Comments Improvements')
        self.assertEqual(datagrid.rows[3]['object'].summary,
                         'Add permission checking for JSON API')

        self.client.logout()

    def testDashboard2(self):
        """Testing dashboard view (outgoing)"""
        self.client.login(username='admin', password='admin')

        response = self.client.get('/dashboard/', {'view': 'outgoing'})
        self.assertEqual(response.status_code, 200)

        datagrid = self.getContextVar(response, 'datagrid')
        self.assert_(datagrid)
        self.assertEqual(len(datagrid.rows), 2)
        self.assertEqual(datagrid.rows[0]['object'].summary,
                         'Interdiff Revision Test')
        self.assertEqual(datagrid.rows[1]['object'].summary,
                         'Add permission checking for JSON API')

        self.client.logout()

    def testDashboard3(self):
        """Testing dashboard view (to-me)"""
        self.client.login(username='doc', password='doc')

        response = self.client.get('/dashboard/', {'view': 'to-me'})
        self.assertEqual(response.status_code, 200)

        datagrid = self.getContextVar(response, 'datagrid')
        self.assert_(datagrid)
        self.assertEqual(len(datagrid.rows), 2)
        self.assertEqual(datagrid.rows[0]['object'].summary,
                         'Made e-mail improvements')
        self.assertEqual(datagrid.rows[1]['object'].summary,
                         'Add permission checking for JSON API')

        self.client.logout()

    def test_dashboard_to_group_with_joined_groups(self):
        """Testing dashboard view with to-group and joined groups"""
        self.client.login(username='doc', password='doc')

        group = Group.objects.get(name='devgroup')
        group.users.add(User.objects.get(username='doc'))

        response = self.client.get('/dashboard/',
                                   {'view': 'to-group',
                                    'group': 'devgroup'})
        self.assertEqual(response.status_code, 200)

        datagrid = self.getContextVar(response, 'datagrid')
        self.assert_(datagrid)
        self.assertEqual(len(datagrid.rows), 2)
        self.assertEqual(datagrid.rows[0]['object'].summary,
                         'Update for cleaned_data changes')
        self.assertEqual(datagrid.rows[1]['object'].summary,
                         'Comments Improvements')

        self.client.logout()

    def test_dashboard_to_group_with_unjoined_public_group(self):
        """Testing dashboard view with to-group and unjoined public group"""
        self.client.login(username='doc', password='doc')

        group = self.create_review_group(name='new-public', invite_only=False)

        review_request = self.create_review_request(summary='Test 1',
                                                    publish=True)
        review_request.target_groups.add(group)

        response = self.client.get('/dashboard/',
                                   {'view': 'to-group',
                                    'group': 'devgroup'})
        self.assertEqual(response.status_code, 200)

    def test_dashboard_to_group_with_unjoined_private_group(self):
        """Testing dashboard view with to-group and unjoined private group"""
        self.client.login(username='doc', password='doc')

        group = self.create_review_group(name='new-private', invite_only=True)

        review_request = self.create_review_request(summary='Test 1',
                                                    publish=True)
        review_request.target_groups.add(group)

        response = self.client.get('/dashboard/',
                                   {'view': 'to-group',
                                    'group': 'new-group'})
        self.assertEqual(response.status_code, 404)

    def testDashboardSidebar(self):
        """Testing dashboard view (to-group devgroup)"""
        self.client.login(username='doc', password='doc')
        user = User.objects.get(username='doc')
        profile = user.get_profile()
        local_site = None

        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)

        counts = self.getContextVar(response, 'sidebar_counts')
        self.assertEqual(
            counts['outgoing'],
            ReviewRequest.objects.from_user(
                user, user, local_site=local_site).count())
        self.assertEqual(
            counts['incoming'],
            ReviewRequest.objects.to_user(user, local_site=local_site).count())
        self.assertEqual(
            counts['to-me'],
            ReviewRequest.objects.to_user_directly(
                user, local_site=local_site).count())
        self.assertEqual(
            counts['starred'],
            profile.starred_review_requests.public(
                user, local_site=local_site).count())
        self.assertEqual(counts['mine'],
            ReviewRequest.objects.from_user(
                user, user, None, local_site=local_site).count())
        self.assertEqual(counts['groups']['devgroup'],
            ReviewRequest.objects.to_group(
                'devgroup', local_site=local_site).count())
        self.assertEqual(counts['groups']['privgroup'],
            ReviewRequest.objects.to_group(
                'privgroup', local_site=local_site).count())

        self.client.logout()

    def testInterdiff(self):
        response = self.client.get('/r/8/diff/1-2/')
            print "Error: %s" % self.getContextVar(response, 'error')
            print self.getContextVar(response, 'trace')
        self.assertEqual(self.getContextVar(response, 'num_diffs'), 3)
        files = self.getContextVar(response, 'files')
        self.assert_(files)
        self.assertEqual(files[0]['depot_filename'],
                         '/trunk/reviewboard/TESTING')
        self.assert_('fragment' in files[0])
        self.assert_('interfilediff' in files[0])
        self.assertEqual(files[1]['depot_filename'],
                         '/trunk/reviewboard/settings_local.py.tmpl')
        self.assert_('fragment' not in files[1])
        self.assert_('interfilediff' in files[1])
    def testInterdiffNewFile(self):
        response = self.client.get('/r/8/diff/2-3/')
            print "Error: %s" % self.getContextVar(response, 'error')
            print self.getContextVar(response, 'trace')
        self.assertEqual(self.getContextVar(response, 'num_diffs'), 3)
        files = self.getContextVar(response, 'files')
        self.assert_(files)
        self.assertEqual(files[0]['depot_filename'],
                         '/trunk/reviewboard/NEW_FILE')
        self.assert_('fragment' in files[0])
        self.assert_('interfilediff' in files[0])

    def testDashboard5(self):
        """Testing dashboard view (mine)"""
        self.client.login(username='doc', password='doc')

        response = self.client.get('/dashboard/', {'view': 'mine'})
        self.assertEqual(response.status_code, 200)

        datagrid = self.getContextVar(response, 'datagrid')
        self.assert_(datagrid)
        self.assertEqual(len(datagrid.rows), 2)
        self.assertEqual(datagrid.rows[0]['object'].summary,
                         'Improved login form')
        self.assertEqual(datagrid.rows[1]['object'].summary,
                         'Comments Improvements')

        self.client.logout()
        review_request = ReviewRequest.objects.get(
            summary="Add permission checking for JSON API")
        filediff = \
            review_request.diffset_history.diffsets.latest().files.all()[0]
        review = Review(review_request=review_request, user=user)
        review.save()

        comment = review.comments.create(filediff=filediff, first_line=1)
        comment.text = 'This is a test'
        comment.issue_opened = True
        comment.issue_status = Comment.OPEN
        comment.num_lines = 1
        comment.save()

    fixtures = ['test_users', 'test_reviewrequests', 'test_scmtools']
    def testDraftChanges(self):
        draft = self.getDraft()
        self.assert_("summary" in fields)
        self.assert_("description" in fields)
        self.assert_("testing_done" in fields)
        self.assert_("branch" in fields)
        self.assert_("bugs_closed" in fields)
        self.assertEqual(set(fields["bugs_closed"]["added"]), new_bugs_norm)
    def getDraft(self):
        """Convenience function for getting a new draft to work with."""
        return ReviewRequestDraft.create(ReviewRequest.objects.get(
            summary="Add permission checking for JSON API"))
class FieldTests(TestCase):
    # Bug #1352
    def testLongBugNumbers(self):
        """Testing review requests with very long bug numbers"""
        review_request = ReviewRequest()
        review_request.bugs_closed = \
            '12006153200030304432010,4432009'
        self.assertEqual(review_request.get_bug_list(),
                         ['4432009', '12006153200030304432010'])
    # Our _("(no summary)") string was failing in the admin UI, as
    # django.template.defaultfilters.stringfilter would fail on a
    # ugettext_lazy proxy object. We can use any stringfilter for this.
    #
    # Bug #1346
    def testNoSummary(self):
        """Testing review requests with no summary"""
        from django.template.defaultfilters import lower
        review_request = ReviewRequest()
        lower(unicode(review_request))
    fixtures = ['test_users', 'test_reviewrequests', 'test_scmtools']
    def testDuplicateReviews(self):

        review_request = ReviewRequest.objects.get(
            summary="Add permission checking for JSON API")
        filediff = \
            review_request.diffset_history.diffsets.latest().files.all()[0]
        review = Review(review_request=review_request, user=user)
        review.body_top = body_top
        review.save()
        master_review = review

        comment = review.comments.create(filediff=filediff, first_line=1)
        comment.text = comment_text_1
        comment.num_lines = 1
        comment.save()
        review = Review(review_request=review_request, user=user)
        review.save()

        comment = review.comments.create(filediff=filediff, first_line=1)
        comment.text = comment_text_2
        comment.num_lines = 1
        comment.save()
        review = Review(review_request=review_request, user=user)
        review.body_bottom = body_bottom
        review.save()

        comment = review.comments.create(filediff=filediff, first_line=1)
        comment.text = comment_text_3
        comment.num_lines = 1
        comment.save()
        self.assert_(review)
        self.assert_(len(default_reviewers) == 2)
        self.assert_(default_reviewer1 in default_reviewers)
        self.assert_(default_reviewer2 in default_reviewers)
        self.assert_(len(default_reviewers) == 1)
        self.assert_(default_reviewer2 in default_reviewers)
        default_reviewers = DefaultReviewer.objects.for_repository(None, test_site)
        self.assert_(len(default_reviewers) == 1)
        self.assert_(default_reviewer1 in default_reviewers)
        self.assert_(len(default_reviewers) == 1)
        self.assert_(default_reviewer2 in default_reviewers)
        """Testing DefaultReviewerForm with a User not on the same LocalSite."""
        """Testing DefaultReviewerForm with a Group not on the same LocalSite."""
        """Testing DefaultReviewerForm with a Repository not on the same LocalSite."""
    def testMilestones(self):
    def testPalindrome(self):
            "{% ifneatnumber " + str(rid) + " %}"
class CounterTests(TestCase):
        """Testing counters with reopening discarded outgoing review requests"""
        """Testing counters with reopening submitted outgoing review requests"""
    fixtures = ['test_users', 'test_reviewrequests', 'test_scmtools',
                'test_site']
        self.assertTrue(group in Group.objects.accessible(self.user))
        self.assertTrue(group in Group.objects.accessible(self.anonymous))
        self.assertFalse(group in Group.objects.accessible(self.user))
        self.assertFalse(group in Group.objects.accessible(self.anonymous))
        self.assertTrue(group in Group.objects.accessible(self.user))
        self.assertFalse(group in Group.objects.accessible(self.anonymous))
        """Testing visibility of review requests assigned to invite-only groups by a non-member"""
        review_request = self._get_review_request()
        review_request.submitter = self.user
        review_request.save()
        """Testing access to a private repository with joined review group added"""
        review_request = self._get_review_request()
        """Testing no access to a review request with only an unjoined invite-only group"""
        review_request = self._get_review_request()
        """Testing access to a review request with specific target user and invite-only group"""
        review_request = self._get_review_request()
        review_request = self._get_review_request()
        review_request.save()

        """Testing access to a review request with a private repository with user added"""
        review_request = self._get_review_request()
        review_request.save()

        """Testing access to a review request with a private repository with review group added"""
        review_request = self._get_review_request()
        review_request.save()

    def _get_review_request(self, local_site=None):
        # Get a review request and clear out the reviewers.
        review_request = ReviewRequest.objects.public(local_site=local_site)[0]
        review_request.target_people.clear()
        review_request.target_groups.clear()
        return review_request

    def testUnicode(self):
        user.first_name = u'Test\u21b9'
        user.last_name = u'User\u2729'