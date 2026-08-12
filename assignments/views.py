from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Assignment
from .serializers import AssignmentSerializer


class AssignmentViewSet(viewsets.GenericViewSet):
    """
    Complete CRUD API for assignments.

    GET     /api/assignments/       -> List all assignments
    POST    /api/assignments/       -> Create an assignment
    GET     /api/assignments/{id}/  -> Get one assignment
    PUT     /api/assignments/{id}/  -> Update an assignment
    PATCH   /api/assignments/{id}/  -> Partially update an assignment
    DELETE  /api/assignments/{id}/  -> Delete an assignment
    """

    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    # GET /api/assignments/
    def list(self, request):
        """Return all assignments."""
        assignments = Assignment.objects.all()
        serializer = AssignmentSerializer(assignments, many=True)
        return Response(serializer.data)

    # POST /api/assignments/
    def create(self, request):
        """Create a new assignment."""
        serializer = AssignmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # GET /api/assignments/{id}/
    def retrieve(self, request, pk=None):
        """Return a single assignment."""
        try:
            assignment = Assignment.objects.get(pk=pk)
        except Assignment.DoesNotExist:
            return Response(
                {"error": "Assignment not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = AssignmentSerializer(assignment)
        return Response(serializer.data)

    # PUT /api/assignments/{id}/
    def update(self, request, pk=None):
        """Fully update an assignment."""
        try:
            assignment = Assignment.objects.get(pk=pk)
        except Assignment.DoesNotExist:
            return Response(
                {"error": "Assignment not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = AssignmentSerializer(
            assignment,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # PATCH /api/assignments/{id}/
    def partial_update(self, request, pk=None):
        """Partially update an assignment."""
        try:
            assignment = Assignment.objects.get(pk=pk)
        except Assignment.DoesNotExist:
            return Response(
                {"error": "Assignment not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = AssignmentSerializer(
            assignment,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # DELETE /api/assignments/{id}/
    def destroy(self, request, pk=None):
        """Delete an assignment."""
        try:
            assignment = Assignment.objects.get(pk=pk)
        except Assignment.DoesNotExist:
            return Response(
                {"error": "Assignment not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        assignment.delete()

        return Response(
            {"message": "Assignment deleted successfully."},
            status=status.HTTP_204_NO_CONTENT
        )